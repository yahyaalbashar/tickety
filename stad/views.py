from django.shortcuts import render,redirect
from django.db.models import Q
from django.conf import settings
from .models import User, Match, Ticket,Arena
from .forms import UserForm,TicketForm,MatchForm
import barcode
from barcode.writer import ImageWriter
from django.contrib import messages

def home(request):

	return render(request,'home.html')

def view_match(request):
	today_matches=Match.objects.filter(match_status=2)
	coming_matches=Match.objects.filter(match_status=1)
	finished_matches=Match.objects.filter(match_status=3)
	match=Match.objects.all()
	match_form=MatchForm(request.GET or None)
	match_status_request=request.GET.get('match_status')
	competition_name_sort=request.GET.get('competition_name')

	if match_status_request == '1':
		match=coming_matches
	elif match_status_request == '2':
		match=today_matches
	elif match_status_request == '3':
		match=finished_matches
	else:
		match=Match.objects.all()
	text_query=request.GET.get('text_q')
	status_query=request.GET.get('stat_q')
	comp_query=request.GET.get('comp_q')
	if text_query or status_query or comp_query :
		match=match.filter(
			Q(competition_name__icontains=text_query)|
			Q(home_team__team_name__icontains=text_query) |
			Q(away_team__team_name__icontains=text_query)|
			Q(match_status=status_query)|
			Q(competition_name=comp_query)
			)

	context={
	'match':match,
	'match_form':match_form,
	'today_matches':today_matches,
	'coming_matches':coming_matches,
	'finished_matches':finished_matches

	}
	return render(request,'view_match.html',context)

def create_user(request):

	match=Match.objects.all()
	ticket=Ticket.objects.all()
	form=UserForm(request.POST or None)
	ticket_form=TicketForm(request.POST or None)
	if form.is_valid():
		instance=form.save(commit=False)
		for obj in match:
			if obj.id ==int(request.POST['match']):
				if obj.ticket_set.count() == obj.stadium.arena_capacity:
					messages.error(request, 'Tickets for this match sold Out')

				else:
					instance.save()
					request.session['user_id']=instance.id
					request.session['match_id']=request.POST['match']
					request.session['ticket_class']=request.POST['ticket_class']
					request.session['payment_method']=request.POST['payment_method']
					return redirect('/ticket/')
	

	context={
	'form':form,
	'match':match,
	'ticket_from':ticket_form,
	}
	return render(request,'usercreate.html',context)

def ticket_purchase(request):
	match=Match.objects.all()
	ticket=Ticket.objects.all()
	user_id=request.session.get('user_id')
	match_id=int(request.session.get('match_id'))
	ticket_class=int(request.session.get('ticket_class'))
	payment_method=int(request.session['payment_method'])
	user_instance=User.objects.all()
	ean = barcode.get('ean13', str(user_id)+'123456789102', writer=ImageWriter())
	
	for obj in match:
		if match_id == obj.id:
			ticket_match=obj

	for obj in user_instance:
		if obj.id == user_id:
			ticket_instance=Ticket.objects.create(
				ticket_price=2,
				reserved_to=obj,
				match=ticket_match,
				payment_method=payment_method,
				ticket_class=ticket_class,
				barcode_image=ean.save(settings.MEDIA_ROOT+'/' + str(user_id))
						)
			if ticket_instance.ticket_class==1:
				ticket_instance.ticket_price*=2
				
			elif ticket_instance.ticket_class==3:
				ticket_instance.ticket_price*=4

	price=ticket_instance.ticket_price

	# for obj in ticket:
	# 	tday=utc.localize(datetime.datetime.today())
	# 	if obj.match.match_date_time > tday:
	# 		ticket.delete()

	context={
	'user_id':user_id,
	'user_instance':user_instance,
	'ticket_instance':ticket_instance,
	'payment_method':payment_method,
	'price':price
	}
	return render(request,'user_ticket.html',context)
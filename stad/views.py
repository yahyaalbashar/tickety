from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponseRedirect
from .models import User, Match, Ticket,Arena
from .forms import UserForm,TicketForm
import barcode
from barcode.writer import ImageWriter
from django.conf import settings
import os
import datetime
import pytz
from django.contrib import messages
def home(request):
	team=User.objects.all()
	greeting='hello'
	context={
	'tempvar':greeting,
	'team':team
	}

	return render(request,'home.html',context)

def view_match(request):
	match=Match.objects.all()
	context={
	'match':match,
	}
	return render(request,'view_match.html',context)

def create_user(request):

	match=Match.objects.all()
	form=UserForm(request.POST or None)
	ticket_form=TicketForm(request.POST or None)
	if form.is_valid():
		instance=form.save(commit=False)
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

def paypal_payment(request):
	return render(request,'purchase.html',{})

def ticket_purchase(request):
	utc=pytz.UTC
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
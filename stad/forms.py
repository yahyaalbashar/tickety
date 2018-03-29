from django import forms
from .models import User,Ticket,Arena,Match
class UserForm(forms.ModelForm):
	class Meta:
		model=User

		fields=[
		'name',
		'phone_no',
		'address',
		'email'
			]	

class TicketForm(forms.ModelForm):
	class Meta:
		model=Ticket
		fields=[
		'ticket_class',
		'match',
		'payment_method'
		]

class MatchForm(forms.ModelForm):
	class Meta:
		model=Match

		fields=[
		'match_status',
		'competition_name'
		]
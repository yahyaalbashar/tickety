from django.db import models
from django.contrib.postgres.fields import ArrayField
MATCH_CHOICES=(
			(1,'Coming'),
			(2,'Today'),
			(3,'Fineshed')
	)
PAYMENT_CHOICES=(
			(0,'Online'),
			(1,'On delivery'),
	)
CLASS_CHOICES=(
			(0,'basic'),
			(1,'mid'),
			(3,'first')
	)
# Create your models here.
class Arena(models.Model):
	arena_name=models.CharField(max_length=250,blank=False)
	location=models.CharField(max_length=250,blank=False)
	arena_capacity=models.IntegerField(default=0)
	size=ArrayField(models.IntegerField(),default=0,null=True)

	def save(self, *args, **kwargs):
		for i in range(1,self.arena_capacity):
			self.size.append(i+1)
		super(Arena, self).save(*args, **kwargs)
	def seat_check(self,seat,*args,**kwargs):
		self.size.remove(seat)
		super(Arena,self).save(*args, **kwargs)



	def __str__(self):
		return self.arena_name
class User(models.Model):
	name=models.CharField(max_length=250,blank=False)
	phone_no=models.CharField(max_length=250,blank=False)
	address=models.CharField(max_length=250,blank=False)
	email=models.EmailField(max_length=254, blank=True)

	def __str__(self):
		return self.name


class Team(models.Model):
	team_name=models.CharField(max_length=250,blank=False)
	team_country=models.CharField(max_length=250,blank=False)
	team_details=models.TextField(null=True)
	def __str__(self):
		return self.team_name


class Match(models.Model):
	match_date_time=models.DateTimeField(null=True)
	match_description=models.TextField(null=True)
	competition_name=models.CharField(max_length=250,blank=True)
	stadium=models.ForeignKey(Arena,on_delete=models.CASCADE,default=1)
	match_status=models.IntegerField(choices=MATCH_CHOICES,default=1)
	home_team=models.ForeignKey(Team,on_delete=models.CASCADE,related_name='hometeam',default=1)
	away_team=models.ForeignKey(Team,on_delete=models.CASCADE,related_name='awayteam',default=2)

	def __str__(self):
		return self.competition_name



class Ticket(models.Model):
	ticket_price=models.IntegerField(blank=False)
	reserved_to=models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
	match=models.ForeignKey(Match,on_delete=models.CASCADE,blank=True,null=True)
	barcode_image=models.ImageField(upload_to='img/',blank=True)
	payment_method=models.CharField(choices=PAYMENT_CHOICES,max_length=250,null=True)
	ticket_class=models.CharField(max_length=250,choices=CLASS_CHOICES,null=True)

	def __str__(self):
		return self.ticket_class



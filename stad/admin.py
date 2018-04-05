from django.contrib import admin
from .models import User, Ticket, Match, Team ,Arena
# Register your models here.
class UserAdminView(admin.ModelAdmin):
	class Meta:
		model=User
	list_display=['__str__','phone_no','address']

class TicketAdminView(admin.ModelAdmin):
	class Meta:
		model=Ticket
	list_display=['reserved_to','ticket_class']
class MatchAdminView(admin.ModelAdmin):
	class Meta:
		model=Match
	list_display=['__str__','home_team','away_team','competition_name','stadium','match_status']
class TeamAdminView(admin.ModelAdmin):
	class Meta:
		model=Team

	list_display=['__str__','team_country']
class ArenaAdminView(admin.ModelAdmin):
	class Meta:
		model=Arena
	list_display=['__str__','location']

admin.site.register(User,UserAdminView)
admin.site.register(Ticket,TicketAdminView)
admin.site.register(Match,MatchAdminView)
admin.site.register(Team,TeamAdminView)
admin.site.register(Arena,ArenaAdminView)

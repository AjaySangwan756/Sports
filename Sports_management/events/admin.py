from django.contrib import admin
from .models import Player, Event, Plan, SportsSchedule

admin.site.register(Player)
admin.site.register(Event)
admin.site.register(Plan)
admin.site.register(SportsSchedule)
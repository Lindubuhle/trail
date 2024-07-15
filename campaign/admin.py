from django.contrib import admin
from .models import Event, Participation

# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'location')
    search_fields = ('name', 'location')

class ParticipationAdmin(admin.ModelAdmin):
    list_display = ('user', 'event')
    list_filter = ('event',)
    search_fields = ('user__username', 'event__name')

admin.site.register(Event, EventAdmin)
admin.site.register(Participation, ParticipationAdmin)


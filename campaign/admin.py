from django.contrib import admin
from .models import Event, Participation

# Register your models here.
class EventAdmin(admin.ModelAdmin):
    """
    Customizes the admin interface for the Event model.
    """ 
    list_display = ('name', 'date', 'location')
    search_fields = ('name', 'location')

class ParticipationAdmin(admin.ModelAdmin):
    """
    Customizes the admin interface for the Participation model.
    """
    list_display = ('user', 'event')
    list_filter = ('event',)
    search_fields = ('user__username', 'event__name')

admin.site.register(Event, EventAdmin)
admin.site.register(Participation, ParticipationAdmin)


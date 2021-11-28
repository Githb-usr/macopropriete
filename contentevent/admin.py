from django.contrib import admin

from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    """
    Display of Event in the back office
    """
    model = Event
    empty_value_display = '-empty-'
    list_display = ('category', 'title', 'content', 'creation_date',
                    'last_edit', 'start_date', 'end_date', 'status',)

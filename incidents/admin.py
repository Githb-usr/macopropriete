from django.contrib import admin

from .models import Incident, IncidentTracking

@admin.register(Incident)
class IncidentAdmin(admin.ModelAdmin):
    """
    Display of Incident in the back office
    """
    model = Incident
    empty_value_display = '-empty-'
    list_display = ('category', 'content', 'creation_date',)

@admin.register(IncidentTracking)
class IncidentTrackingAdmin(admin.ModelAdmin):
    """
    Display of IncidentTracking in the back office
    """
    list_display = ('status', 'status_date',)

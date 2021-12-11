from django.contrib import admin

from .models import Zone

class ZoneAdmin(admin.ModelAdmin):
    """
    Display of Zone in the back office
    """
    list_display = ('code', 'name', 'description', 'image',)


admin.site.register(Zone, ZoneAdmin)
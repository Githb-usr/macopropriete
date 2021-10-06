from django.contrib import admin

from .models import Condominium, Lot, Zone

class CondominiumAdmin(admin.ModelAdmin):
    """
    Display of Condominium in the back office
    """
    list_display = ('condominium_type', 'name', 'number', 'description',
                    'share', 'image')

class LotAdmin(admin.ModelAdmin):
    """
    Display of Lot in the back office
    """
    list_display = ('lot_type', 'number', 'description',
                    'share', 'image')

class ZoneAdmin(admin.ModelAdmin):
    """
    Display of Zone in the back office
    """
    list_display = ('code', 'name', 'description', 'image',)

admin.site.register(Condominium, CondominiumAdmin)
admin.site.register(Lot, LotAdmin)
admin.site.register(Zone, ZoneAdmin)

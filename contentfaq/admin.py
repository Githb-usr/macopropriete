from django.contrib import admin

from .models import Faq

@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    """
    Display of FAQ in the back office
    """
    model = Faq
    empty_value_display = '-empty-'
    list_display = ('category', 'question', 'answer',
                    'creation_date', 'last_edit', 'status',)

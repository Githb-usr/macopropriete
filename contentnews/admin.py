from django.contrib import admin

from .models import News

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    """
    Display of News in the back office
    """
    model = News
    empty_value_display = '-empty-'
    list_display = ('title', 'content', 'category', 'creation_date',
                    'display_author', 'last_edit', 'status',)

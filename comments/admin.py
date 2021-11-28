from django.contrib import admin

from .models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Display of Comment in the back office
    """
    model = Comment
    empty_value_display = '-empty-'
    list_display = ('content', 'creation_date', 'status',)

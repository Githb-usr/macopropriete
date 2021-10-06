from django.contrib import admin

from .models import Article, Faq, Event, Incident, IncidentTracking, Comment

class ArticleAdmin(admin.ModelAdmin):
    """
    Display of Article in the back office
    """
    list_display = ('title', 'content', 'image', 'creation_date',
                    'last_edit', 'status',)

class FaqAdmin(admin.ModelAdmin):
    """
    Display of FAQ in the back office
    """
    list_display = ('faq_section', 'question', 'answer', 'image',
                    'creation_date', 'last_edit', 'status',)

class EventAdmin(admin.ModelAdmin):
    """
    Display of Event in the back office
    """
    list_display = ('title', 'content', 'image', 'creation_date',
                    'last_edit', 'start_date', 'end_date', 'status',)

class IncidentAdmin(admin.ModelAdmin):
    """
    Display of Incident in the back office
    """
    list_display = ('incident_type', 'content', 'image', 'creation_date',)

class IncidentTrackingAdmin(admin.ModelAdmin):
    """
    Display of IncidentTracking in the back office
    """
    list_display = ('status', 'status_date',)

class CommentAdmin(admin.ModelAdmin):
    """
    Display of Comment in the back office
    """
    list_display = ('content', 'creation_date', 'status',)

admin.site.register(Article, ArticleAdmin)
admin.site.register(Faq, FaqAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Incident, IncidentAdmin)
admin.site.register(IncidentTracking, IncidentTrackingAdmin)
admin.site.register(Comment, CommentAdmin)
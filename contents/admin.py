from django.contrib import admin

from .models import News, Faq, Event, Incident, IncidentTracking, Comment

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    """
    Display of News in the back office
    """
    model = News
    empty_value_display = '-empty-'
    list_display = ('title', 'content', 'category', 'image', 'creation_date',
                    'display_author', 'last_edit', 'status',)

@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    """
    Display of FAQ in the back office
    """
    model = Faq
    empty_value_display = '-empty-'
    list_display = ('category', 'question', 'answer', 'image',
                    'creation_date', 'last_edit', 'status',)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    """
    Display of Event in the back office
    """
    model = Event
    empty_value_display = '-empty-'
    list_display = ('category', 'title', 'content', 'image', 'creation_date',
                    'last_edit', 'start_date', 'end_date', 'status',)

@admin.register(Incident)
class IncidentAdmin(admin.ModelAdmin):
    """
    Display of Incident in the back office
    """
    model = Incident
    empty_value_display = '-empty-'
    list_display = ('category', 'content', 'image', 'creation_date',)

@admin.register(IncidentTracking)
class IncidentTrackingAdmin(admin.ModelAdmin):
    """
    Display of IncidentTracking in the back office
    """
    list_display = ('status', 'status_date',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Display of Comment in the back office
    """
    model = Comment
    empty_value_display = '-empty-'
    list_display = ('content', 'creation_date', 'status',)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
from django.contrib import messages
from django.shortcuts import redirect, render
from django.utils import timezone
from django.views.generic import DetailView, ListView

from contentevent.forms import EventForm, EventDeleteForm, EventUpdateForm
from contentevent.models import Event
from contentevent.settings import EVENT_CREATION_SUCCESS, EVENT_DELETE_SUCCESS, EVENT_UPDATE_SUCCESS

class EventListNewView(ListView):
    model = Event
    paginate_by = 8
    template_name = 'contentevent/event_list_new.html'
    context_object_name = 'event_list_new'

    def get_queryset(self):
        current_datetime = timezone.now()
        return Event.objects.filter(start_date__gt=current_datetime).filter(status='ACTIVATED').order_by('start_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_number = self.request.GET.get('page', 1)
        context['page_range_top'] = context['paginator'].get_elided_page_range(number=page_number, on_each_side=1, on_ends=1)
        context['page_range_bottom'] = context['paginator'].get_elided_page_range(number=page_number, on_each_side=1, on_ends=1)
        return context

class EventListOldView(ListView):
    model = Event
    paginate_by = 8
    template_name = 'contentevent/event_list_old.html'
    context_object_name = 'event_list_old'

    def get_queryset(self):
        current_datetime = timezone.now()
        return Event.objects.filter(start_date__lt=current_datetime).filter(status='ACTIVATED').order_by('-start_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_number = self.request.GET.get('page', 1)
        context['page_range_top'] = context['paginator'].get_elided_page_range(number=page_number, on_each_side=1, on_ends=1)
        context['page_range_bottom'] = context['paginator'].get_elided_page_range(number=page_number, on_each_side=1, on_ends=1)
        return context

class EventDetailView(DetailView):
    model = Event
    template_name = 'contentevent/event_detail.html'
    context_object_name = 'event_detail'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

    def get_object(self, queryset=None):
        # To use uuid in the route
        return Event.objects.get(uuid=self.kwargs.get("uuid"))

def event_create_view(request):
    event_form = EventForm()

    if request.method == 'POST':
        event_form = EventForm(request.POST)
        if event_form.is_valid():
            event = event_form.save(commit=False)
            event.author = request.user
            event.save()
            messages.success(request, EVENT_CREATION_SUCCESS) # Adding a confirmation message
            return redirect('event-detail', uuid=event.uuid)

    context = {
        'event_form': event_form,
    }
            
    return render(request, 'contentevent/event_create.html', context=context)

def event_update_view(request, uuid):
    event = Event.objects.get(uuid=uuid)
    event_data = {
        'category': event.category,
        'title': event.title,
        'content': event.content,
        'start_date': event.start_date,
        'end_date': event.end_date,
        'status': event.status,
    }
    event_form = EventForm(initial=event_data)
    event_update_form = EventUpdateForm()

    if request.method == 'POST':
        event_form = EventForm(request.POST, instance=event)
        event_update_form = EventUpdateForm(request.POST)
        if all([event_form.is_valid() and event_update_form.is_valid()]):
            event = event_form.save()
            event_update = event_update_form.save(commit=False)
            event_update.event = event
            event_update.updater = request.user
            event_update.save()
            messages.success(request, EVENT_UPDATE_SUCCESS) # Adding a confirmation message
            return redirect('event-detail', uuid=event.uuid)

    context = {
        'event': event,
        'event_form': event_form,
        'event_update_form': event_update_form,
    }
            
    return render(request, 'contentevent/event_update.html', context=context)

def event_delete_view(request, uuid):
    event = Event.objects.get(uuid=uuid)
    event_delete_form = EventDeleteForm()
    current_datetime = timezone.now()

    if request.method == 'POST':
        event_delete_form = EventDeleteForm(request.POST)
    if event_delete_form.is_valid():
        event_delete = event_delete_form.save(commit=False)
        event_delete.event = event
        event_delete.deleter = request.user
        event_delete.save()
        event.status = 'DELETED'
        event.save()
        messages.success(request, EVENT_DELETE_SUCCESS) # Adding a confirmation message
        if event.start_date <= current_datetime:
            return redirect('event-list-old')
        else: 
            return redirect('event-list-new')
        
    context = {
        'event': event,
        'event_delete_form': event_delete_form,
    }
            
    return render(request, 'contentevent/event_delete.html', context=context)

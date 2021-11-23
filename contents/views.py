#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import DeleteView, DetailView, ListView, UpdateView
from django.views.generic.base import TemplateView
from django.views.generic.edit import ModelFormMixin

from contents.choices import FAQ_CATEGORY
from contents.forms import EventForm, FaqForm, NewsForm, NewsUpdateForm, PhotoForm
from contents.models import Event, Faq, News, NewsUpdate
from contents.settings import EVENT_CREATION_SUCCESS, NEWS_CREATION_SUCCESS, NEWS_UPDATE_SUCCESS, QUESTION_CREATION_SUCCESS
from pages.utils import choice_translation

class NewsListView(ListView):
    model = News
    paginate_by = 5
    template_name = 'contents/news_list.html'
    context_object_name = 'news_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_number = self.request.GET.get('page', 1)
        context['page_range_top'] = context['paginator'].get_elided_page_range(number=page_number, on_each_side=1, on_ends=1)
        context['page_range_bottom'] = context['paginator'].get_elided_page_range(number=page_number, on_each_side=1, on_ends=1)
        return context

class NewsDetailView(DetailView):
    model = News
    template_name = 'contents/news_detail.html'
    context_object_name = 'news_detail'

    def get_object(self, queryset=None):
        # To use uuid in the route
        return News.objects.get(uuid=self.kwargs.get("uuid"))

def news_create_view(request):
    news_form = NewsForm()
    photo_form = PhotoForm()

    if request.method == 'POST':
        news_form = NewsForm(request.POST)
        photo_form = PhotoForm(request.POST, request.FILES)
        if all([news_form.is_valid() and photo_form.is_valid()]):
            news = news_form.save(commit=False)
            news.author = request.user
            news.save()
            photo = photo_form.save(commit=False)
            photo.uploader = request.user
            photo.save()
            news.photos.add(photo)
            news.save()
            messages.success(request, NEWS_CREATION_SUCCESS) # Adding a confirmation message
            return redirect('news-detail', uuid=news.uuid)

    context = {
        'news_form': news_form,
        'photo_form': photo_form,
    }
            
    return render(request, 'contents/news_create.html', context=context)

def news_update_view(request, uuid):
    news = News.objects.get(uuid=uuid)
    news_data = {
        'category': news.category,
        'title': news.title,
        'content': news.content,
        'status': news.status,
    }
    news_form = NewsForm(initial=news_data)
    news_update_form = NewsUpdateForm()
    photo_form = PhotoForm()

    if request.method == 'POST':
        news_form = NewsForm(request.POST, instance=news)
        news_update_form = NewsUpdateForm(request.POST)
        photo_form = PhotoForm(request.POST, request.FILES)
        if all([news_form.is_valid() and news_update_form.is_valid() and photo_form.is_valid()]):
            news = news_form.save()
            news_update = news_update_form.save(commit=False)
            news_update.news = news
            news_update.updater = request.user
            news_update.save()
            photo = photo_form.save(commit=False)
            photo.uploader = request.user
            photo.save()
            news.photos.add(photo)
            news.save()
            messages.success(request, NEWS_UPDATE_SUCCESS) # Adding a confirmation message
            return redirect('news-detail', uuid=news.uuid)

    context = {
        'news': news,
        'news_form': news_form,
        'news_update_form': news_update_form,
        'photo_form': photo_form,
    }
            
    return render(request, 'contents/news_update.html', context=context)

class NewsDeleteView(SuccessMessageMixin, DeleteView):
    model = News
    template_name = 'contents/news_delete.html'
    success_message = 'La news a bien été supprimée !'
    success_url = reverse_lazy('author-list')

    def get_object(self, queryset=None):
        # To use uuid in the route
        return News.objects.get(uuid=self.kwargs.get("uuid"))

class FaqCategoryListView(TemplateView):
    template_name = 'contents/faq_category_list.html'

class FaqCategoryView(ListView):
    model = Faq
    paginate_by = 5
    template_name = 'contents/faq_category.html'
    context_object_name = 'faq_category'
    
    def get_queryset(self):
        return Faq.objects.filter(category=self.kwargs['category'].upper())

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        current_cat = choice_translation(FAQ_CATEGORY, self.kwargs['category'].upper())
        context['current_category'] = current_cat
        page_number = self.request.GET.get('page', 1)
        context['page_range_top'] = context['paginator'].get_elided_page_range(number=page_number, on_each_side=1, on_ends=1)
        context['page_range_bottom'] = context['paginator'].get_elided_page_range(number=page_number, on_each_side=1, on_ends=1)
        return context

def faq_create_view(request):
    faq_form = FaqForm()
    photo_form = PhotoForm()

    if request.method == 'POST':
        faq_form = FaqForm(request.POST)
        photo_form = PhotoForm(request.POST, request.FILES)
        if all([faq_form.is_valid() and photo_form.is_valid()]):
            question = faq_form.save(commit=False)
            question.author = request.user
            question.save()
            photo = photo_form.save(commit=False)
            photo.uploader = request.user
            photo.save()
            question.photos.add(photo)
            question.save()
            messages.success(request, QUESTION_CREATION_SUCCESS) # Adding a confirmation message
            return redirect('faq-category', category=question.category.lower())

    context = {
        'faq_form': faq_form,
        'photo_form': photo_form,
    }
            
    return render(request, 'contents/faq_create.html', context=context)

def faq_update_view(request, uuid):
    news = News.objects.get(uuid=uuid)
    news_data = {
        'category': news.category,
        'title': news.title,
        'content': news.content,
        'status': news.status,
    }
    news_form = NewsForm(initial=news_data)
    news_update_form = NewsUpdateForm()
    photo_form = PhotoForm()

    if request.method == 'POST':
        news_form = NewsForm(request.POST, instance=news)
        news_update_form = NewsUpdateForm(request.POST)
        photo_form = PhotoForm(request.POST, request.FILES)
        if all([news_form.is_valid() and news_update_form.is_valid() and photo_form.is_valid()]):
            news = news_form.save()
            news_update = news_update_form.save(commit=False)
            news_update.news = news
            news_update.updater = request.user
            news_update.save()
            photo = photo_form.save(commit=False)
            photo.uploader = request.user
            photo.save()
            news.photos.add(photo)
            news.save()
            messages.success(request, NEWS_UPDATE_SUCCESS) # Adding a confirmation message
            return redirect('news-detail', uuid=news.uuid)

    context = {
        'news': news,
        'news_form': news_form,
        'news_update_form': news_update_form,
        'photo_form': photo_form,
    }
            
    return render(request, 'contents/news_update.html', context=context)

class EventListNewView(ListView):
    model = Event
    paginate_by = 8
    template_name = 'contents/event_list_new.html'
    context_object_name = 'event_list_new'

    def get_queryset(self):
        current_datetime = timezone.now()
        return Event.objects.filter(start_date__gt=current_datetime).order_by('start_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_number = self.request.GET.get('page', 1)
        context['page_range_top'] = context['paginator'].get_elided_page_range(number=page_number, on_each_side=1, on_ends=1)
        context['page_range_bottom'] = context['paginator'].get_elided_page_range(number=page_number, on_each_side=1, on_ends=1)
        return context

class EventListOldView(ListView):
    model = Event
    paginate_by = 8
    template_name = 'contents/event_list_old.html'
    context_object_name = 'event_list_old'

    def get_queryset(self):
        current_datetime = timezone.now()
        return Event.objects.filter(start_date__lt=current_datetime).order_by('-start_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_number = self.request.GET.get('page', 1)
        context['page_range_top'] = context['paginator'].get_elided_page_range(number=page_number, on_each_side=1, on_ends=1)
        context['page_range_bottom'] = context['paginator'].get_elided_page_range(number=page_number, on_each_side=1, on_ends=1)
        return context

class EventDetailView(DetailView):
    model = Event
    template_name = 'contents/event_detail.html'
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
    photo_form = PhotoForm()

    if request.method == 'POST':
        event_form = EventForm(request.POST)
        photo_form = PhotoForm(request.POST, request.FILES)
        if all([event_form.is_valid() and photo_form.is_valid()]):
            event = event_form.save(commit=False)
            event.author = request.user
            event.save()
            photo = photo_form.save(commit=False)
            photo.uploader = request.user
            photo.save()
            event.photos.add(photo)
            event.save()
            messages.success(request, EVENT_CREATION_SUCCESS) # Adding a confirmation message
            return redirect('event-detail', uuid=event.uuid)

    context = {
        'event_form': event_form,
        'photo_form': photo_form,
    }
            
    return render(request, 'contents/event_create.html', context=context)

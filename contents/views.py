#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy
from datetime import datetime
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.generic import DetailView, ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from contents.choices import FAQ_CATEGORY
from contents.models import Event, Faq, News, NewsUpdate
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

class NewsCreateView(SuccessMessageMixin, CreateView):
    model = News
    template_name = 'contents/news_create.html'
    success_message = 'Votre news a bien été créée !'
    fields = ['category', 'title', 'content', 'image', 'status']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class NewsUpdateView(SuccessMessageMixin, UpdateView):
    model = News
    template_name = 'contents/news_update.html'
    success_message = 'La news a bien été mise à jour !'
    fields = ['category', 'title', 'content', 'image', 'status']

    def get_object(self, queryset=None):
        # To use uuid in the route
        return News.objects.get(uuid=self.kwargs.get("uuid"))

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class NewsDeleteView(SuccessMessageMixin, DeleteView):
    model = News
    template_name = 'contents/news_delete.html'
    success_message = 'La news a bien été supprimée !'
    success_url = reverse_lazy('author-list')

    def get_object(self, queryset=None):
        # To use uuid in the route
        return News.objects.get(uuid=self.kwargs.get("uuid"))

class FaqCategoryView(TemplateView):
    template_name = 'contents/faq_category.html'

class FaqListView(ListView):
    paginate_by = 5
    template_name = 'contents/faq_list.html'
    context_object_name = 'faq_list'

    def get_queryset(self):
        return Faq.objects.filter(category=self.kwargs['category'].upper())

    def get_context_data(self, **kwargs):
        faq_cat = choice_translation(FAQ_CATEGORY, 'category')
        context = super().get_context_data(**kwargs)
        page_number = self.request.GET.get('page', 1)
        context['category'] = faq_cat
        context['page_range_top'] = context['paginator'].get_elided_page_range(number=page_number, on_each_side=1, on_ends=1)
        context['page_range_bottom'] = context['paginator'].get_elided_page_range(number=page_number, on_each_side=1, on_ends=1)
        return context

class FaqDetailView(DetailView):
    model = Faq
    template_name = 'contents/faq_detail.html'
    context_object_name = 'faq_detail'

    def get_object(self, queryset=None):
        # To use uuid in the route
        return Faq.objects.get(uuid=self.kwargs.get("uuid"))

class EventListNewView(ListView):
    model = Event
    paginate_by = 8
    template_name = 'contents/event_list_new.html'
    context_object_name = 'event_list_new'

    def get_queryset(self):
        current_datetime = datetime.now()
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
        current_datetime = datetime.now()
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

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy
import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.urls import reverse
from django.utils import timezone
from django.views.generic import DetailView, ListView
import json
import logging

from contents.models import Article, Faq, Event

class NewsListView(ListView):
    model = Article
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
    model = Article
    template_name = 'contents/news_detail.html'
    context_object_name = 'news_detail'

    def get_object(self, queryset=None):
        # To use uuid in the route
        return Article.objects.get(uuid=self.kwargs.get("uuid"))

class FaqListView(ListView):
    model = Faq
    paginate_by = 5
    template_name = 'contents/faq_list.html'
    context_object_name = 'faq_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_number = self.request.GET.get('page', 1)
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

class EventListView(ListView):
    model = Event
    paginate_by = 5
    template_name = 'contents/event_list.html'
    context_object_name = 'event_list'

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

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

class NewsDetailView(DetailView):
    model = Article
    template_name = 'contents/news_detail.html'
    context_object_name = 'news_detail'

class FaqListView(ListView):
    model = Faq
    paginate_by = 5
    template_name = 'contents/faq_list.html'
    context_object_name = 'faq_list'

class FaqDetailView(DetailView):
    model = Faq
    template_name = 'contents/faq_detail.html'
    context_object_name = 'faq_detail'
    
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView

from contentnews.forms import NewsForm, NewsDeleteForm, NewsUpdateForm
from contentnews.models import News
from contentnews.settings import NEWS_CREATION_SUCCESS, NEWS_DELETE_SUCCESS,\
    NEWS_UPDATE_SUCCESS

class NewsListView(ListView):
    model = News
    paginate_by = 5
    template_name = 'contentnews/news_list.html'
    context_object_name = 'news_list'

    def get_queryset(self):
        return News.objects.filter(status='ACTIVATED')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_number = self.request.GET.get('page', 1)
        context['page_range_top'] = context['paginator'].get_elided_page_range(
            number=page_number,
            on_each_side=1,
            on_ends=1
        )
        context['page_range_bottom'] = context['paginator'].get_elided_page_range(
            number=page_number,
            on_each_side=1,
            on_ends=1
        )
        return context

class NewsDetailView(DetailView):
    slug_url_kwarg = 'uuid'
    slug_field = 'uuid'
    model = News
    template_name = 'contentnews/news_detail.html'
    context_object_name = 'news_detail'

def news_create_view(request):
    news_form = NewsForm()

    if request.method == 'POST':
        news_form = NewsForm(request.POST)
        if news_form.is_valid():
            news = news_form.save(commit=False)
            news.author = request.user
            news.save()
            messages.success(request, NEWS_CREATION_SUCCESS)  # Adding a confirmation message
            return redirect('news-detail', uuid=news.uuid)

    context = {
        'news_form': news_form,
    }

    return render(request, 'contentnews/news_create.html', context=context)

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

    if request.method == 'POST':
        news_form = NewsForm(request.POST, instance=news)
        news_update_form = NewsUpdateForm(request.POST)
        if all([news_form.is_valid() and news_update_form.is_valid()]):
            news = news_form.save()
            news_update = news_update_form.save(commit=False)
            news_update.news = news
            news_update.updater = request.user
            news_update.save()
            messages.success(request, NEWS_UPDATE_SUCCESS)  # Adding a confirmation message
            return redirect('news-detail', uuid=news.uuid)

    context = {
        'news': news,
        'news_form': news_form,
        'news_update_form': news_update_form,
    }

    return render(request, 'contentnews/news_update.html', context=context)

def news_delete_view(request, uuid):
    news = News.objects.get(uuid=uuid)
    news_delete_form = NewsDeleteForm()

    if request.method == 'POST':
        news_delete_form = NewsDeleteForm(request.POST)
    if news_delete_form.is_valid():
        news_delete = news_delete_form.save(commit=False)
        news_delete.news = news
        news_delete.deleter = request.user
        news_delete.save()
        news.status = 'DELETED'
        news.save()
        messages.success(request, NEWS_DELETE_SUCCESS)  # Adding a confirmation message
        return redirect('news-list')

    context = {
        'news': news,
        'news_delete_form': news_delete_form,
    }

    return render(request, 'contentnews/news_delete.html', context=context)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.views.generic.base import TemplateView

from contentfaq.forms import FaqForm, FaqDeleteForm, FaqUpdateForm
from contentfaq.models import Faq
from contentfaq.settings import FAQ_CATEGORY, QUESTION_CREATION_SUCCESS,\
    QUESTION_DELETE_SUCCESS, QUESTION_UPDATE_SUCCESS
from pages.utils import choice_translation

class FaqCategoryListView(TemplateView):
    template_name = 'contentfaq/faq_category_list.html'

class FaqCategoryView(ListView):
    model = Faq
    paginate_by = 5
    template_name = 'contentfaq/faq_category.html'
    context_object_name = 'faq_category'

    def get_queryset(self):
        try:
            return Faq.objects.filter(category=self.kwargs['category'].upper()).filter(status='ACTIVATED')
        except Faq.objects.filter(category=self.kwargs['category'].upper().filter(status='ACTIVATED')).DoesNotExist:
            return Faq.objects.none()

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        current_cat = choice_translation(FAQ_CATEGORY, self.kwargs['category'].upper())
        context['current_category'] = current_cat
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

def faq_create_view(request):
    faq_form = FaqForm()

    if request.method == 'POST':
        faq_form = FaqForm(request.POST)
        if faq_form.is_valid():
            question = faq_form.save(commit=False)
            question.author = request.user
            question.save()
            # Adding a confirmation message
            messages.success(request, QUESTION_CREATION_SUCCESS)
            return redirect('faq-category', category=question.category.lower())

    context = {
        'faq_form': faq_form,
    }

    return render(request, 'contentfaq/faq_create.html', context=context)

def faq_update_view(request, uuid):
    question = Faq.objects.get(uuid=uuid)
    question_data = {
        'category': question.category,
        'question': question.question,
        'answer': question.answer,
        'status': question.status,
    }
    faq_form = FaqForm(initial=question_data)
    faq_update_form = FaqUpdateForm()

    if request.method == 'POST':
        faq_form = FaqForm(request.POST, instance=question)
        faq_update_form = FaqUpdateForm(request.POST)
        if all([faq_form.is_valid() and faq_update_form.is_valid()]):
            question = faq_form.save()
            question_update = faq_update_form.save(commit=False)
            question_update.faq = question
            question_update.updater = request.user
            question_update.save()
            # Adding a confirmation message
            messages.success(request, QUESTION_UPDATE_SUCCESS)
            return redirect('faq-category', category=question.category.lower())

    context = {
        'question': question,
        'faq_form': faq_form,
        'faq_update_form': faq_update_form,
    }

    return render(request, 'contentfaq/faq_update.html', context=context)

def faq_delete_view(request, uuid):
    question = Faq.objects.get(uuid=uuid)
    faq_delete_form = FaqDeleteForm()

    if request.method == 'POST':
        faq_delete_form = FaqDeleteForm(request.POST)
    if faq_delete_form.is_valid():
        faq_delete = faq_delete_form.save(commit=False)
        faq_delete.faq = question
        faq_delete.deleter = request.user
        faq_delete.save()
        question.status = 'DELETED'
        question.save()
        # Adding a confirmation message
        messages.success(request, QUESTION_DELETE_SUCCESS)
        return redirect('faq-category', category=question.category.lower())

    context = {
        'question': question,
        'faq_delete_form': faq_delete_form,
    }

    return render(request, 'contentfaq/faq_delete.html', context=context)

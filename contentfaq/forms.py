#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.forms import ModelForm

from contentfaq import models

class FaqForm(ModelForm):
    """
    Form used for create a FAQ question
    """
    class Meta:
        model = models.Faq
        fields = ('category', 'question', 'answer', 'status', )

class FaqUpdateForm(ModelForm):
    class Meta:
        model = models.FaqUpdate
        fields = ('update_reason',)

class FaqDeleteForm(ModelForm):
    class Meta:
        model = models.FaqDelete
        fields = ('deletion_reason',)

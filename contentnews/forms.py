#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.forms import ModelForm

from contentnews import models

class NewsForm(ModelForm):
    """
    Form used for create a news
    """
    class Meta: 
        model = models.News
        fields = ('category', 'title', 'content', 'status', )

class NewsUpdateForm(ModelForm):
    class Meta: 
        model = models.NewsUpdate
        fields = ('update_reason',)

class NewsDeleteForm(ModelForm):
    class Meta: 
        model = models.NewsDelete
        fields = ('deletion_reason',)

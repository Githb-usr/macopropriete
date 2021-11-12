#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms

from contents import models

class NewsForm(forms.ModelForm):
    """
    Form used for the profile update
    """
    class Meta: 
        model = models.News
        fields = ('category', 'title', 'content', 'image', 'status', )

class NewsUpdateForm(forms.ModelForm):
    class Meta: 
        model = models.NewsUpdate
        fields = ('update_reason',)

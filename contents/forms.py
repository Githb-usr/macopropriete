#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms

from contents import models

class PhotoForm(forms.ModelForm):
    """
    Form used for photo upload
    """
    class Meta:
        model = models.Photo
        fields = ['image', 'caption']

class NewsForm(forms.ModelForm):
    """
    Form used for the profile update
    """
    class Meta: 
        model = models.News
        fields = ('category', 'title', 'content', 'status', )

class NewsUpdateForm(forms.ModelForm):
    class Meta: 
        model = models.NewsUpdate
        fields = ('update_reason',)

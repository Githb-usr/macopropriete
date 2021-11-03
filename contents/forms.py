#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms

from contents.models import News, NewsDelete, NewsUpdate

class NewsUpdateForm(forms.ModelForm):
    """
    Form used for the profile update
    """
    class Meta: 
        model = News
        fields = ('category', 'title', 'content', 'image', 'status')

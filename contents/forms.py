#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.forms import ModelForm, SplitDateTimeField, widgets

from contents import models

class PhotoForm(ModelForm):
    """
    Form used for photo upload
    """
    class Meta:
        model = models.Photo
        fields = ('image', 'caption')

    def __init__(self, *args, **kwargs):
        super(PhotoForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = False

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

class FaqForm(ModelForm):
    """
    Form used for create a FAQ question
    """
    class Meta: 
        model = models.Faq
        fields = ('category', 'question', 'answer', 'status', )

class EventForm(ModelForm):
    """
    Form used for create an event
    """
    start_date = SplitDateTimeField(
        label='Début de l\'évènement (Date / Heure)',
        widget=widgets.SplitDateTimeWidget(
            date_attrs={'type': 'date', 'style': 'width:25%;'},
            time_attrs={'type': 'time', 'style': 'width:25%;'},
            date_format='%d/%m/%Y',
            time_format="'%H:%M'"),
    )
    end_date = SplitDateTimeField(
        label='Fin de l\'évènement (Date / Heure)',
        widget=widgets.SplitDateTimeWidget(
            date_attrs={'type': 'date', 'style': 'width:25%;'},
            time_attrs={'type': 'time', 'style': 'width:25%;'},
            date_format='%d/%m/%Y',
            time_format="'%H:%M'"),
    )
    class Meta: 
        model = models.Event
        fields = ('category', 'title', 'content', 'start_date', 'end_date', 'status', )

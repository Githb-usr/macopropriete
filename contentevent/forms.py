#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.forms import ModelForm, SplitDateTimeField, widgets

from contentevent import models

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

class EventUpdateForm(ModelForm):
    class Meta: 
        model = models.EventUpdate
        fields = ('update_reason',)

class EventDeleteForm(ModelForm):
    class Meta: 
        model = models.EventDelete
        fields = ('deletion_reason',)

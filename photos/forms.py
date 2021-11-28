#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.forms import ModelForm

from photos import models

class PhotoForm(ModelForm):
    """
    Photo upload
    """
    class Meta:
        model = models.Photo
        fields = ('image', 'caption')

    def __init__(self, *args, **kwargs):
        super(PhotoForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = True

# -*- coding: utf-8 -*-

from djtools import forms
from .models import *


class AcessoBiometricoForm(forms.ModelFormPlus):

    class Meta:
        model = AcessoBiometrico
        exclude = []

    class Media:
        js = ('/static/systi/js/acesso_biometrico.js',)
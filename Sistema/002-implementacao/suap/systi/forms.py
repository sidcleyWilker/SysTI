# -*- coding: utf-8 -*-

from djtools import forms
from django.utils import timezone
from .models import *


class AcessoBiometricoForm(forms.ModelFormPlus):

    class Meta:
        model = AcessoBiometrico
        exclude = []

    class Media:
        js = ('/static/systi/js/acesso_biometrico.js',)

    def clean(self):
        self.cleaned_data['data_registro'] = timezone.now()
        return self.cleaned_data

    def clean_servidor(self):
        usuario = self.cleaned_data.get('tipo_do_usuario')
        servidor = self.cleaned_data.get('servidor')
        if (usuario == 'Servidor' and (servidor == '' or servidor == None)):
            raise forms.ValidationError('Selecione um Servidor')
        return servidor

    def clean_aluno(self):
        usuario = self.cleaned_data.get('tipo_do_usuario')
        aluno = self.cleaned_data.get('aluno')
        if ((usuario == 'Aluno') and ((aluno == '' or aluno == None))):
            raise forms.ValidationError('Selecione um Aluno')
        return aluno
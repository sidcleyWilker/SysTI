# -*- coding: utf-8 -*-

from djtools import forms
from django.utils import timezone
from .models import *


class AtivoForm(forms.ModelFormPlus):
    class Meta:
        model = Ativo
        exclude = []


class AcessoBiometricoForm(forms.ModelFormPlus):

    class Meta:
        model = AcessoBiometrico
        exclude = []

    class Media:
        js = ('/static/systi/js/acesso_biometrico.js',)


    def clean(self):
        data_des_registro = self.cleaned_data['data_des_registro']

        if data_des_registro == None or data_des_registro == '':
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


class TransferenciaForm(forms.ModelFormPlus):

    class Meta:
        model = Transferencia
        exclude = []

    class Media:
        js = ('/static/systi/js/transferencia.js',)


    # def clean(self):
    #     data = self.cleaned_data.get('data_solicitacao')
    #     if data == None:
    #         data = timezone.now()

    def clean_anexo_motivo(self):
        anexo = self.cleaned_data.get('anexo_motivo')

        if anexo == None:
            raise ValidationError("Selecione algum Arquivo!")

        if anexo.size >= 3090000:
            raise ValidationError("Arquivo exedeu o tamnaho permitido!")

        return anexo

    def clean_termo_recebimento(self):
        anexo = self.cleaned_data.get('termo_recebimento')

        if anexo == None:
            raise ValidationError("Selecione algum Arquivo!")

        if anexo.size >= 3090000:
            raise ValidationError("Arquivo exedeu o tamnaho permitido!")

        return anexo

class MaterialForm(forms.ModelFormPlus):

    class Meta:
        model = Material
#        exclude = []


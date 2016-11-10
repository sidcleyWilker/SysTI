# -*- coding: utf-8 -*-

from djtools import forms
from .models import Ativo


class AtivoForm(forms.ModelFormPlus):

    observacoes = forms.CharFieldPlus(
        widget=forms.Textarea(),
        label=u'Observações',
        required=False)


    class Meta:
        model = Ativo
        exclude = []



    #escolha = forms.ModelChoiceFieldPlus2( widget=forms.RadioSelect, choices=CHOICES)


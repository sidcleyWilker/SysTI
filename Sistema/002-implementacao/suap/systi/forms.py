# -*- coding: utf-8 -*-

from djtools import forms
from django.utils import timezone
from .models import *
from rh.models import Setor
from djtools.formwidgets import TreeWidget

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
        exclude = []

    def clean(self):
        nome_material = self.cleaned_data.get("nome_material")
        tipo_material = self.cleaned_data.get("tipo_material")
        local_guardado = self.cleaned_data.get("local_guardado")
        descricao = self.cleaned_data.get("descricao")
        unidade_de_medida = self.cleaned_data.get("unidade_de_medida")
        quantidade = self.cleaned_data.get("quantidade")
        fornecedor = self.cleaned_data.get("fornecedor")
        self.cleaned_data['data_registro'] = timezone.now()


        if nome_material==None or tipo_material==None or local_guardado==None or descricao==None or unidade_de_medida==None or quantidade==None or fornecedor==None:
            raise forms.ValidationError('Os Campos Devem ser Preenchidos Corretamente')

        return self.cleaned_data

class EmprestimoForm(forms.ModelFormPlus):

    class Meta:
        model = Emprestimo
        exclude = []

    def clean(self):
        ativo = self.cleaned_data.get("ativo")
        motivo = self.cleaned_data.get("motivo")
        data_emprestimo = self.cleaned_data.get("data_emprestimo")
        data_devolucao = self.cleaned_data.get("data_devolucao")
        estado = self.cleaned_data.get("estado")
        setor_origem = self.cleaned_data.get("setor_origem")
        setor_destino = self.cleaned_data.get("setor_destino")

        if ativo==None or motivo==None or data_emprestimo==None or data_devolucao==None or estado==None or setor_origem==None or setor_destino==None:
            raise forms.ValidationError('Os Campos Devem ser Preenchidos Corretamente')

        #Valida a data das operações de empréstimos
        data_emprestimo = self.cleaned_data.get("data_emprestimo")
        data_devolucao = self.cleaned_data.get("data_devolucao")

        if data_emprestimo > data_devolucao:
            raise forms.ValidationError('A data de empréstimo deve ser inferior a data de devolução')

        #Valida a origem e o destino do ativo/material
        if setor_origem == setor_destino:
            raise forms.ValidationError('Um ativo/material não pode ser emprestado para o mesmo local')

        return self.cleaned_data

class ServicoInternoForm(forms.ModelFormPlus):

    class Meta:
        model = ServicoInterno
        exclude = []

    class Media:
        js = ('/static/systi/js/servico_interno_externo.js',)

class ServicoExternoForm(forms.ModelFormPlus):

    class Meta:
        model = ServicoExterno
        exclude = []

    class Media:
        js = ('/static/systi/js/servico_interno_externo.js',)



class CompartimentoForms(forms.ModelFormPlus):

    class Meta:
        model = Compartimento

    setor_suap = forms.ModelChoiceField(Setor.objects, label=u'Hierarquia do Compartimento', widget=TreeWidget(), required=False, help_text=u'Local onde o Compartimento está')


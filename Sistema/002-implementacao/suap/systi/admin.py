# -*- coding: utf-8 -*-

from django.contrib import admin
from djtools.adminutils import ModelAdminPlus
from .models import Ativo, Fornecedor, CategoriaHardware, CategoriaSoftware, CategoriaRede, AcessoBiometrico
from .forms import *


class AtivoHardwareStackedInline(admin.StackedInline):
    model = CategoriaHardware
    fields = ('fabricante', 'versao')
    extra = 1

class AtivoSoftwareStackedInline(admin.StackedInline):
    model = CategoriaSoftware
    fields = ('nome_software', 'versao_software', 'pago')
    extra = 1

class AtivoRedeStackedInline(admin.StackedInline):
    model = CategoriaRede
    fields = ('fabricante', 'versao', 'numero_portas')
    extra = 1

class AtivoAdmin(ModelAdminPlus):
    search_fields = ['nome', 'tombamento', 'numero_etiqueta']
    list_display = ['nome', 'tombamento', 'fornecedor', 'local_do_ativo']
    list_filter = ['nome', 'tombamento', 'numero_etiqueta', 'fornecedor']
    list_display_icons = True
    inlines = [AtivoHardwareStackedInline, AtivoRedeStackedInline, AtivoSoftwareStackedInline]

    fieldsets = (
        (u'Dados do Ativo', {
            'fields': ('nome', 'tombamento', 'numero_etiqueta', 'numero_serie', 'numero_produto')
        }),
        (u'Selecione o Fornecedor', {
            'fields': ('fornecedor',)
        }),
        (u'Selecione o Local do Ativo', {
            'fields': ('local_do_ativo',)
        })
    )



class FornecedorAdmin(ModelAdminPlus):
    search_fields = ['nome', 'email']
    list_filter = ['nome', 'email']
    list_display = ['nome', 'email', 'telefone1']
    list_display_icons = True

    fieldsets = (
        (None, {
            'fields': ('nome', 'cpf', 'cnpj')
        }),
        (u'Informações de Contato', {
            'fields': (('telefone1', 'telefone2'), 'email')
        }),
    )

class AcessoBiometricoAdmin(ModelAdminPlus):
    search_fields = ['id_usuario_fechadura', 'data_registro', 'tipo_do_usuario']
    list_filter = ['id_usuario_fechadura', 'data_registro','tipo_do_usuario']
    list_display = ['id_usuario_fechadura', 'data_registro', 'tipo_do_usuario']
    list_display_icons = True
    form = AcessoBiometricoForm



admin.site.register(Ativo, AtivoAdmin)
admin.site.register(Fornecedor, FornecedorAdmin)
admin.site.register(AcessoBiometrico ,AcessoBiometricoAdmin)
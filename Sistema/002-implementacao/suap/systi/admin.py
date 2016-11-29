# -*- coding: utf-8 -*-

from django.contrib import admin
from django import forms
from djtools.adminutils import ModelAdminPlus
from .models import *
from .forms import *
from djtools.templatetags.djtools_templatetags import view_object_icon


class AtivoAdmin(ModelAdminPlus):
    search_fields = ['nome', 'tombamento', 'numero_etiqueta']
    list_display = ['nome', 'tombamento', 'fornecedor', 'local_do_ativo']
    list_filter = ['nome', 'tombamento', 'numero_etiqueta', 'fornecedor']
    list_display_icons = True
    form = AtivoForm


    fieldsets = (
        (u'Dados do Ativo', {
            'fields': ('nome', 'tombamento', 'numero_etiqueta', 'numero_serie',
                       'numero_produto', 'categoria_do_ativo','fornecedor',
                       'local_do_ativo','mais_atributo')
        }),
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
    list_filter = ['id_usuario_fechadura', 'data_registro', 'tipo_do_usuario']
    list_display = ['id_usuario_fechadura', 'data_registro', 'tipo_do_usuario']
    list_display_icons = True
    form = AcessoBiometricoForm

    def show_list_display_icons(self, obj):
        out = [u'<ul class="list-display-icons">']
        icons_html = [view_object_icon(obj)]
        # Não exibe botão de editar
        # if self.has_change_permission(self.request, obj):
        #    icons_html.append(edit_object_icon(obj))
        for icon_html in icons_html:
            if icon_html:
                out.append(u'<li>%s</li>' % icon_html)
        out.append(u'</ul>')
        return u''.join(out)


    show_list_display_icons.allow_tags = True
    show_list_display_icons.short_description = u'#'



class AtributoInline(admin.StackedInline):
    model = Atributo
    extra = 1


class CategoriaAdmin(ModelAdminPlus):
    search_fields = ['nome']
    list_filter = ['nome', 'descricao']
    list_display = ['nome', 'descricao']
    list_display_icons = True
    inlines = [AtributoInline]


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Ativo, AtivoAdmin)
admin.site.register(Fornecedor, FornecedorAdmin)
admin.site.register(AcessoBiometrico ,AcessoBiometricoAdmin)
# -*- coding: utf-8 -*-

from django.contrib import admin
from django import forms
from djtools.adminutils import ModelAdminPlus
from .models import *
from .forms import *
from djtools.templatetags.djtools_templatetags import view_object_icon

class AtivoFormSet(forms.models.BaseInlineFormSet):

    def clean(self):
        for form in self.forms:
            cleaned_data = form.cleaned_data
            categoria = cleaned_data.get('categoria_do_ativo')

            if categoria == 'Hardware':
                fabricante = self.cleaned_data.get('fabricante', None)
                versao = self.cleaned_data.get('versao', None)
                if fabricante == '' or fabricante == None:
                    raise forms.ValidationError('Preencha com o nome do fabricante')
                if versao == '' or versao == None:
                    raise forms.ValidationError(u'Preencha com a versão do Hardware')


class AtivoHardwareStackedInline(admin.StackedInline):
    model = CategoriaHardware
    form = CategoriaHardwareForm
    formset = AtivoFormSet
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

class AtributoStackedInline(admin.StackedInline):
    model = Atributo
    fields = ('nome_campo', 'tipo_campo', ('obrigatorio', 'unico'), 'valor')
    extra = 1

class AtivoAdmin(ModelAdminPlus):
    search_fields = ['nome', 'tombamento', 'numero_etiqueta']
    list_display = ['nome', 'tombamento', 'fornecedor', 'local_do_ativo']
    list_filter = ['nome', 'tombamento', 'numero_etiqueta', 'fornecedor']
    list_display_icons = True
    form = AtivoForm
    inlines = [AtributoStackedInline, AtivoHardwareStackedInline, AtivoRedeStackedInline, AtivoSoftwareStackedInline]

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



admin.site.register(Ativo, AtivoAdmin)
admin.site.register(Fornecedor, FornecedorAdmin)
admin.site.register(AcessoBiometrico ,AcessoBiometricoAdmin)
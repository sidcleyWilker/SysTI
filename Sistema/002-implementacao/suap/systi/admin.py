# -*- coding: utf-8 -*-

from django.contrib import admin
from django import forms

from comum.utils import get_uo
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
                       'local_do_ativo')
        }),
    )



class FornecedorAdmin(ModelAdminPlus):
    search_fields = ['nome', 'email']
    list_filter = ['nome', 'email']
    list_display = ['nome', 'email', 'telefone1']
    list_display_icons = True

    fieldsets = (
        (None, {
            'fields': ('nome', 'tipo', 'cpf', 'cnpj')
        }),
        (u'Informações de Contato', {
            'fields': (('telefone1', 'telefone2'), 'email')
        }),
    )

    form = FornecedorForm

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

class MaterialAdmin(ModelAdminPlus):
    search_fields = ['nome_material', 'tipo_material',]
    list_filter = ['tipo_material', 'local_guardado',]
    list_display = ['nome_material','tipo_material','local_guardado', 'quantidade']
    list_display_icons = True
    list_per_page = 10
    export_to_xls = True

    fieldsets = (
        (None, {
            'fields': ('nome_material', 'tipo_material','local_guardado',
                       'descricao', 'unidade_de_medida', 'fornecedor', 'estoque_minimo',)
        }),
    )

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

    #Exibir apenas icone de editar
    #def show_list_display_icons(self, obj):
    #    out = [u'<ul class="list-display-icons">']
    #    out.append(u'<li><a class="icon-edit" href="/systi/material/%d/" title="Editar"> Editar </a></li>' % obj.id)
    #    out.append(u'</ul>')

    #    return u''.join(out)

    #show_list_display_icons.allow_tags = True
    #show_list_display_icons.short_description = u'#'

    form = MaterialForm

class CompartimentoAdmin(ModelAdminPlus):
    search_fields = ['codigo_compartimento', 'descricao',]
    list_filter = ['codigo_compartimento','descricao',]
    list_display = ['codigo_compartimento', 'descricao', 'pai',]
    list_display_icons = True

    fieldsets = (
        (None, {
            'fields': ('codigo_compartimento', 'descricao', 'pai',)
        }),
    )

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

class TransferenciaAdmin(ModelAdminPlus):
    search_fields = ['motivo_transferencia']
    list_filter = ['motivo_transferencia', 'data_solicitacao', 'data_transferencia', 'altorizada', 'transferida']
    list_display = ['motivo_transferencia', 'data_solicitacao', 'altorizada', 'transferida']
    list_display_icons = True
    form = TransferenciaForm

    fieldsets = (
        (u'Motivos da Transferencia', {
            'fields': ('motivo_transferencia', 'anexo_motivo', 'chamado', 'descricao',)
        }),
        (u'Ativos a serem transferidos', {
            'fields': ('ativos_transferidos', 'setor_destino',)
        }),
        (u'Dados da Transferencia', {
            'fields': ('termo_recebimento', 'data_solicitacao', ('altorizada', 'data_altorizada'), ('transferida', 'data_transferencia'))
        }),
    )

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

class EmprestimoAdmin(ModelAdminPlus):
    search_fields = ['ativo', 'motivo', 'data_emprestimo',
                       'data_devolucao', 'estado', 'setor_origem',
                       'setor_destino',]
    list_filter = ['data_emprestimo', 'data_devolucao', 'estado',]
    list_display = ['motivo', 'data_emprestimo',
                       'data_devolucao', 'estado',]
    list_display_icons = True

    fieldsets = (
        (None, {
            'fields': ('ativo', 'motivo', 'data_emprestimo',
                       'data_devolucao', 'estado', 'setor_origem',
                       'setor_destino',)
        }),
    )

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

    form = EmprestimoForm

class ServicosInternosAdmin(ModelAdminPlus):
    search_fields = ['motivo_servico', 'data_diagnostico', 'tipo_servico', 'estado_servico',]
    list_filter = ['motivo_servico', 'data_diagnostico', 'tipo_servico', 'estado_servico']
    list_display = ['motivo_servico', 'data_diagnostico', 'tipo_servico', 'estado_servico',]
    list_display_icons = True

    fieldsets = (
        (None, {
            'fields': ('motivo_servico', 'anexo_motivo', 'chamado',
                       'data_diagnostico', 'diagnostico', 'procedimentos_realizados',
                       'tipo_servico', 'estado_servico', 'motivo_cancel_ou_suspen',
                       'ordem_servico', 'equipamentos_enviados', 'materiais_utilizados',
                       'data_prevista_conclusao')
        }),
    )


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

    form = ServicoInternoForm

class ServicosExternosAdmin(ModelAdminPlus):
    search_fields = ['diagnostico', 'data_diagnostico', 'tipo_servico', 'estado_servico',]
    list_filter = ['diagnostico', 'data_diagnostico', 'tipo_servico', 'estado_servico']
    list_display = ['diagnostico', 'data_diagnostico', 'tipo_servico', 'estado_servico',
                    'data_do_envio', 'data_prevista_devolucao']
    list_display_icons = True

    fieldsets = (
        (None, {
            'fields': ('motivo_servico', 'anexo_motivo', 'chamado', 'equipamentos_enviados',
                    'diagnostico', 'data_diagnostico', 'tipo_servico',
                       'estado_servico', 'motivo_cancel_ou_suspen',
                       'ordem_servico', 'prestador', 'data_prevista_devolucao',)
        }),
    )

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

    form = ServicoExternoForm

admin.site.register(Transferencia, TransferenciaAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Ativo, AtivoAdmin)
admin.site.register(Fornecedor, FornecedorAdmin)
admin.site.register(AcessoBiometrico ,AcessoBiometricoAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(Compartimento, CompartimentoAdmin)
admin.site.register(Emprestimo, EmprestimoAdmin)
admin.site.register(ServicoInterno, ServicosInternosAdmin)
admin.site.register(ServicoExterno, ServicosExternosAdmin)

admin.site.register(Entrada_Material)

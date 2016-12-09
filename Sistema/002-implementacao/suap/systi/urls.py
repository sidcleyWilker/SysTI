# -*- coding: utf-8 -*-
from django.conf.urls import patterns
from .views import AtivoAdd

urlpatterns = patterns('systi.views',

    #(r'^ativo/(?P<id>\d+)/$', 'ativo_detail'),
    (r'^fornecedor/(?P<id>\d+)/$', 'fornecedor_detail'),

    (r'^material/(?P<id>\d+)/$', 'material_detail'),

    (r'^acesso_biometrico/(?P<id>\d+)/$', 'acesso_biometrico_detail'),
    (r'^acessobiometrico/desregistra/(?P<id>\d+)/$', 'acesso_biometrico_desregistra'),


    (r'^teste$', 'AtivoAdd'),

    (r'^transferencia/(?P<id>\d+)/$', 'transferencia_detail'),
    (r'^transferencia/altorizar/(?P<id>\d+)/$', 'transferencia_altorizar'),
    (r'^transferencia/transferir/(?P<id>\d+)/$', 'transferencia_transferir'),

    (r'^teste$', 'AtivoAdd'),
    (r'^compartimentos/(?P<id>\d+)/$', 'compartimento_detail'),


)

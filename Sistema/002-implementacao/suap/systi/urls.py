# -*- coding: utf-8 -*-
from django.conf.urls import patterns
from .views import AtivoAdd

urlpatterns = patterns('systi.views',

    #(r'^ativo/(?P<id>\d+)/$', 'ativo_detail'),
    (r'^fornecedor/(?P<id>\d+)/$', 'fornecedor_detail'),

    (r'^acesso_biometrico/(?P<id>\d+)/$', 'acesso_biometrico_detail'),

    (r'^acessobiometrico/desregistra/(?P<id>\d+)/$', 'acesso_biometrico_desregistra'),

    (r'^teste$', 'AtivoAdd'),


)
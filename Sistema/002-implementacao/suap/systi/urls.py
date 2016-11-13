# -*- coding: utf-8 -*-
from django.conf.urls import patterns

urlpatterns = patterns('systi.views',

    (r'^ativo/(?P<id>\d+)/$', 'ativo_detail'),
    (r'^fornecedor/(?P<id>\d+)/$', 'fornecedor_detail'),
    (r'^acessobiometrico/(?P<id>\d+)/$', 'acessobiometrico_detail'),


)
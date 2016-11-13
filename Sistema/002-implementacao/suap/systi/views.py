# -*- coding: utf-8 -*-


from django.http import Http404
from .models import Fornecedor, Ativo, AcessoBiometrico
from djtools.utils import rtr


@rtr()
def fornecedor_detail(request, id):
    try:
        forne= Fornecedor.objects.get(pk=id)
        ativos = Ativo.objects.filter(fornecedor=id)

    except Fornecedor.DoesNotExist:
        raise Http404(u"Fornecedor não existe.")

    return locals()

@rtr()
def ativo_detail(request, id):
    try:
        ativo = Ativo.objects.get(pk=id)
    except Ativo.DoesNotExist:
        raise Http404(u"Ativo não existe.")

    return locals()


@rtr
def acessobiometrico_detail(request, id):
    try:
        print '############ ############## ##################'
        acesso = AcessoBiometrico.objects.get(pk=id)
        print '############       '+ acesso.id_usuario_fechadura+ '##################'
    except AcessoBiometrico.DoesNoExist:
        raise Http404(u"Acesso Não existe")

    return locals()
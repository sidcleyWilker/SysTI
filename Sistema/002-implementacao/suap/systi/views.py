# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import Http404
from .models import Fornecedor, Ativo
from djtools.utils import rtr
from django.shortcuts import get_object_or_404

@rtr()
def fornecedor_detail(request, id):
    try:
        forne= Fornecedor.objects.get(pk=id)

        ativos = Ativo.objects.filter(fornecedor=id)
        print (ativos)

    except Fornecedor.DoesNotExist:
        raise Http404("Fornecedor não existe.")

    return locals()

@rtr()
def ativo_detail(request, id):
    try:
        ativo = Ativo.objects.get(pk=id)
    except Ativo.DoesNotExist:
        raise Http404("Ativo não existe.")

    return locals()

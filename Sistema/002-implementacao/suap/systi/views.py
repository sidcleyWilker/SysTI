# -*- coding: utf-8 -*-


from django.http import Http404
from .models import Fornecedor, Ativo, AcessoBiometrico, Atributo, Categoria, \
    CategoriaHardware, CategoriaRede, CategoriaSoftware
from djtools.utils import rtr, httprr
from django.utils import timezone


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
        atributos = Atributo.objects.filter(instancia_id=ativo.id)

        try:
            categoria = Categoria.objects.get(instancia_id=ativo.id)
        except:
            pass

        try:
            hardware = CategoriaHardware.objects.get(categoria_ptr_id=categoria.id)
        except:
            pass
        try:
            software = CategoriaSoftware.objects.get(categoria_ptr_id=categoria.id)
        except:
            pass
        try:
            rede = CategoriaRede.objects.get(categoria_ptr_id=categoria.id)
        except:
            pass


    except Ativo.DoesNotExist:
        raise Http404(u"Ativo não existe.")

    return locals()


@rtr()
def acesso_biometrico_detail(request, id):
    try:
        acesso = AcessoBiometrico.objects.get(pk=id)
    except AcessoBiometrico.DoesNoExist:
        raise Http404(u"Acesso Não existe")
    return locals()


def acesso_biometrico_desregistra(request, id):
    acesso = AcessoBiometrico.objects.get(pk=id)
    acesso.data_des_registro = timezone.now()
    acesso.save()
    return httprr('/systi/acesso_biometrico/' + id + '/', u'Acesso Biometrico Concluido.', 'success')
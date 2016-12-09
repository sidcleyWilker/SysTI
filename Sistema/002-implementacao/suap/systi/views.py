# -*- coding: utf-8 -*-


from django.http import Http404
from .models import Fornecedor, Ativo, AcessoBiometrico, Atributo, Categoria
from djtools.utils import rtr, httprr
from django.utils import timezone
from django.shortcuts import render
from .forms import AtivoForm

@rtr()
def fornecedor_detail(request, id):
    try:
        forne= Fornecedor.objects.get(pk=id)
        ativos = Ativo.objects.filter(fornecedor=id)

    except Fornecedor.DoesNotExist:
        raise Http404(u"Fornecedor não existe.")

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



def AtivoAdd(request):

    if request.method == 'POST':
        ativoForm = AtivoForm(request.POST)
    else:
        ativoForm = AtivoForm()

    context = {
        'ativoForm': ativoForm
    }
    template_name = 'AtivoAdd.html'
    return render(request, template_name, context)


@rtr()
def material_detail(request, id):
    try:
        material = Material.objects.get(pk=id)

    except Material.DoesNotExist:
        raise Http404(u"Material não existe.")
    return locals()

@rtr()
def compartimento_detail(request, id):
    try:
        compartimento = Compartimento.objects.get(pk=id)

    except Material.DoesNotExist:
        raise Http404(u"Compartimento não existe.")
    return locals()

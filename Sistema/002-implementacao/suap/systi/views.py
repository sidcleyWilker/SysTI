# -*- coding: utf-8 -*-


from django.http import Http404
from .models import Fornecedor, Ativo, AcessoBiometrico, Atributo, Categoria, Transferencia
from djtools.utils import rtr, httprr
from django.utils import timezone
from django.shortcuts import render
from .forms import AtivoForm
from .choices import SysTIChoices

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
def transferencia_detail(request, id):
    try:
        transferencia = Transferencia.objects.get(pk=id)
        ativos = transferencia.ativos_transferidos.all()
    except Transferencia.DoesNoExist:
        raise Http404(u"Acesso Não existe")
    return locals()

def transferencia_altorizar(request, id):
    try:
        transferencia = Transferencia.objects.get(pk=id)
        transferencia.data_altorizada = timezone.now()
        transferencia.altorizada = SysTIChoices.ALTORIZADO
        transferencia.transferida = SysTIChoices.AGUARDANDO_TRANSFERENCIA
        transferencia.save()
        return httprr('/systi/transferencia/' + id + '/', u'Transferencia Alterada.', 'success')
    except Transferencia.DoesNoExist:
        raise Http404(u"Transferencia Não existe")


def transferencia_transferir(request, id):
    try:
        transferencia = Transferencia.objects.get(pk=id)
        transferencia.data_transferencia = timezone.now()
        transferencia.transferida = SysTIChoices.TRANSFERIDA
        transferencia.save()
        ativos = transferencia.ativos_transferidos.all()

        for ativo in ativos:
            ativo.local_do_ativo = transferencia.setor_destino
            ativo.save()


        return httprr('/systi/transferencia/' + id + '/', u'Transferencia Alterada.', 'success')
    except Transferencia.DoesNoExist:
        raise Http404(u"Transferencia Não existe")
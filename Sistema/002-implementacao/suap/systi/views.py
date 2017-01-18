# -*- coding: utf-8 -*-


from django.http import Http404

from systi.models import ServicoExterno
from .models import Fornecedor, Ativo, AcessoBiometrico, Atributo, Categoria, Transferencia, Emprestimo, Compartimento, Material, ServicoInterno
from djtools.utils import rtr, httprr
from django.utils import timezone
from django.shortcuts import render
from .forms import AtivoForm, MaterialForm
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

@rtr()
def material_detail(request, id):

    try:
        material = Material.objects.get(pk=id)
        fornecedor = material.fornecedor
    except material.DoesNoExist:
        raise Http404(u"Material Não existe")

    return locals()

@rtr()
def compartimento_detail(request, id):
    try:
        compartimento = Compartimento.objects.get(pk=id)

    except Compartimento.DoesNotExist:
        raise Http404(u"Compartimento não existe.")
    return locals()

@rtr()
def emprestimo_detail(request, id):
    try:
        emprestimo = Emprestimo.objects.get(pk=id)
        ativo = emprestimo.ativo
    except emprestimo.DoesNotExist:
        raise Http404(u'Empréstimo não existe')

    return locals()

@rtr()
def servicointerno_detail(request, id):
    try:
        servico_interno = ServicoInterno.objects.get(pk=id)
        equipamentos = servico_interno.equipamentos_enviados.all()
        materiais = servico_interno.materiais.all()

    except ServicoInterno.DoesNotExist:
        raise Http404(u"Servico Interno não existe.")
    return locals()


@rtr()
def servicosexternos_detail(request, id):
    try:
        servico_externo = ServicoExterno.objects.get(pk=id)
    except servico_externo.DoesNotExist:
        raise Http404(u'Serviço Externo não Existe')

    return locals()

def emprestimovigente(request, id):
    try:
        emprestimo = Emprestimo.objects.get(pk=id)
        emprestimo.estado = SysTIChoices.VIGENTE
        Emprestimo.save()

        return httprr('/systi/emprestimo/' + id + '/', u'Emprestimo Vigente.', 'success')
    except Transferencia.DoesNoExist:
        raise Http404(u"Emprestimo Não existe")

def iniciar_servico(request, id):
    try:
        servico_interno = ServicoInterno.objects.get(pk=id)
        servico_interno.data_realizacao = timezone.now()
        servico_interno.save()
        return httprr('/systi/servicointerno/' + id + '/', u'Serviço Interno Alterado.', 'success')
    except ServicoInterno.DoesNotExist:
        raise Http404(u"Servico Interno não existe.")

def registrar_devolucao(request, id):
    try:
        servico_interno = ServicoInterno.objects.get(pk=id)
        servico_interno.data_devolucao = timezone.now()
        servico_interno.save()
        return httprr('/systi/servicointerno/' + id + '/', u'Serviço Interno Alterado.', 'success')
    except ServicoInterno.DoesNotExist:
        raise Http404(u"Servico Interno não existe.")

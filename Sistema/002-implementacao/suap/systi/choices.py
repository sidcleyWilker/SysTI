# -*- coding: utf-8 -*-
from .models import *



class SysTIChoices:

    def __init__(self):
        pass

    def get_value(self, key):
        todos = {}
        todos.update(self.TIPOS_SOLICITACAO)
        return todos.get(key)



    MEMORANDO = u'Memorando'
    CHAMADO = u'Chamado'
    EMAIL = u'E-mail'

    TIPOS_SOLICITACAO = {
        CHAMADO: u'Chamado',
        MEMORANDO: u'Memorando',
        EMAIL: u'E-mail',
    }

    AGUARDANDO_ALTORIZACAO = u'Aguardando Altorização'
    ALTORIZADO = u'Altorizado(a)'

    TRANSFERENCIA_ALTORIZACAO = {
        AGUARDANDO_ALTORIZACAO: u'Aguardando Altorização',
        ALTORIZADO: u'Altorizado(a)'
    }

    AGUARDANDO_TRANSFERENCIA = u'Aguardando Transferencia'
    TRANSFERIDA = u'Transferida(o)'

    TRANSFERENCIAS = {
        AGUARDANDO_ALTORIZACAO: u'Aguardando Altorização',
        AGUARDANDO_TRANSFERENCIA: u'Aguardando Transferencia',
        TRANSFERIDA: u'Transferida(o)'
    }

    AGUARDANDO_DIAGNOSTICO = u'Aguardando Diagnóstico'
    RECOLHIDO = u'Recolhido'
    DEVOLVIDO = u'Devolvido'
    CANCELADO = u'Cacelado'
    EM_EXECUCAO = u'Em Execução'
    SUSPENSO = u'Suspenso'

    ESTADOS_SERVICO = {
        AGUARDANDO_DIAGNOSTICO: u'Aguardando Diagnóstico',
        RECOLHIDO: u'Recolhido',
        DEVOLVIDO: u'Devolvido',
        CANCELADO: u'Cancelado',
        EM_EXECUCAO: u'Em Execução',
        SUSPENSO: u'Suspenso',
    }

    EM_ABERTO = u'Em Aberto'
    AGUARDANDO_TERMO = u'Aguardando Termo'
    SOLICITADO = u'Solicitado'
    DEVOLVIDO = u'Devolvido'
    VIGENTE = u'Vigente'
    PENDENTE = u'Pendente'

    ESTADO_EMPRESTIMOS = {
        EM_ABERTO: u'Em Aberto',
        AGUARDANDO_TERMO: u'Aguardando Termo',
        SOLICITADO: u'Solicitado',
        DEVOLVIDO: u'Devolvido',
        VIGENTE: u'Vigente',
        PENDENTE: u'Pendente',
    }

    PESSOA_FISICA = u'Pessoa Física'
    PESSOA_JURIDICA = u'Pessoa Jurídica'

    TIPO_FORNECEDOR = {
        PESSOA_FISICA: u'Pessoa Física',
        PESSOA_JURIDICA: u'Pessoa Jurídica',
    }
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
    CHAMADO =  u'Chamdo'
    EMAIL = u'E-mail'

    TIPOS_SOLICITACAO = {
        CHAMADO: u'Chamdo',
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
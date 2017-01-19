# -*- coding: utf-8 -*-

import os
from djtools.db import models
from djtools.models import ModelPlus
from .choices import SysTIChoices
from django.core.exceptions import ValidationError

DOCUMENT_EXTENSIONS = ['pdf', 'txt', 'doc', 'dot', 'docx', 'odt']
IMAGE_EXTENSIONS = ['bmp', 'jpeg', 'jpg', 'png']

stados_do_usuario = {
    'Ativo': 'Ativo',
    'Inativo': 'Inativo'
}

TIPO_USUARIO = {
    'Aluno': 'Aluno',
    'Servidor': 'Servidor',
    'Servidor Terceirizado': 'Servidor Terceirizado',
}

categorias = {
    'Software': 'Software',
    'Rede':'Rede',
    'Hardware':'Hardware'
}

escolhas = {
    'Data': 'Data',
    'Texto': 'Texto',
    'Inteiro': 'Inteiro',
    'Float': 'Float'

}

sim_nao = {
    'Sim': 'Sim',
    u'Não': u'Não'
}


UNIDADE_MEDIDA = {
    'Cm' : 'Centimetro',
    'Mt' : 'Metro',
    'Lt' : 'Litro',
    'Und' : 'Unidade',
    'Cx' : 'Caixa',
    'Pc' : 'Pacote',
}

TIPO_SERVICO = {
    'Suporte' : 'Suporte',
    'Manutencao' : 'Manutenção',
}



class Fornecedor(ModelPlus):
    nome = models.CharFieldPlus(verbose_name=u'Nome do Fornecedor', max_length=30)
    cpf = models.BrCpfField(verbose_name=u'CPF', blank=True, null=True)
    cnpj = models.BrCnpjField(verbose_name=u'CNPJ', blank=True, null=True)
    telefone1 = models.BrTelefoneField(verbose_name=u'Telefone para Contato')
    telefone2 = models.BrTelefoneField(verbose_name=u'Telefone para Contato Reserva', blank=True, null=True)
    email = models.EmailField(verbose_name=u'E-mail para Contato')

    class Meta:
        verbose_name = u'Fornecedor'
        verbose_name_plural = u'Fornecedores'

    def get_absolute_url(self):
        return '/systi/fornecedor/{}/'.format(self.id)

    def __str__(self):
        return self.nome


class Ativo(ModelPlus):
    nome = models.CharFieldPlus(verbose_name=u'Nome do Ativo', max_length=30)
    tombamento = models.CharFieldPlus(verbose_name=u'Numero de Tombamento', max_length=30)
    numero_etiqueta = models.CharFieldPlus(verbose_name=u'Numero da Etiqueta', max_length=30)
    numero_serie = models.CharFieldPlus(verbose_name=u'Numero da Serie', max_length=30)
    numero_produto = models.CharFieldPlus(verbose_name=u'Numero do Produto', max_length=30)
    fornecedor = models.ForeignKeyPlus('systi.Fornecedor',verbose_name=u'Fornecedor')
    local_do_ativo = models.ForeignKeyPlus('comum.Sala', verbose_name=u'Local do Ativo')
    categoria_do_ativo = models.ForeignKey('systi.Categoria', verbose_name=u'Categoria')

    class Meta:
        verbose_name = u'Ativo'
        verbose_name_plural = u'Ativos'


    def get_absolute_url(self):
        return '/systi/ativo/{}/'.format(self.id)

    def __str__(self):
        return self.nome



class Atributo(ModelPlus):
    nome_campo = models.CharFieldPlus(verbose_name=u'Nome do Campo', max_length=30)
    tipo_campo = models.CharFieldPlus(
        verbose_name=u'Tipo do campo',
        max_length=30,
        choices=escolhas.items(),
        default=escolhas.get('Texto')
    )
    obrigatorio = models.BooleanField(verbose_name=u'Obrigatorio', default=False)
    unico = models.BooleanField(verbose_name=u'È unico', default=False)
    valor = models.CharField(verbose_name=u'Valor', max_length=50)
    categoria_instancia = models.ForeignKey('systi.Categoria', verbose_name=u'Instancia')

    class Meta:
        verbose_name = u'Campo Adicional'
        verbose_name_plural = u'Campos Adicionais'


# class ValorAtt(models.Model):
#     att = models.ForeignKey(Atributo)
#     modelo = models.ForeignKey(Ativo)
#     valor = models.CharField(max_length=30)


class Categoria(ModelPlus):
    nome = models.CharFieldPlus(verbose_name=u'Nome da Categoria', max_length=30, help_text=u'Ex: Hardware, Software, Rede ...')
    descricao = models.TextField(verbose_name=u'Descrição', max_length=30)


    class Meta:
        verbose_name = u'Categoria'
        verbose_name_plural = u'Categorias'

    def get_absolute_url(self):
        return '/systi/categoria/{}/'.format(self.id)


class AcessoBiometrico(ModelPlus):
    id_usuario_fechadura = models.CharFieldPlus(verbose_name=u'Identificação Na Fechadura', max_length=40)
    data_registro = models.DateFieldPlus(verbose_name=u'Data do Registro', blank=True, null=True)
    data_des_registro = models.DateFieldPlus(u'Data do des-registro', blank=True, null=True)
    local_da_fechadura = models.ForeignKeyPlus('comum.Sala', verbose_name=u'Local do Fechadura')
    tipo_do_usuario = models.CharFieldPlus(verbose_name=u'Tipo do Usuário', max_length=25, choices=TIPO_USUARIO.items(), default=TIPO_USUARIO.get('Aluno'))
    aluno = models.ForeignKeyPlus('edu.Aluno', verbose_name=u'Aluno', blank=True, null=True)
    servidor = models.ForeignKeyPlus('rh.Servidor', verbose_name=u'Servidor do IF', blank=True, null=True)
    servidor_terceirizado = models.CharFieldPlus(verbose_name=u'Nome do Servidor ou Visitante', blank=True, null=True)

    class Meta:
        verbose_name = u'Acesso Biometrico'
        verbose_name_plural = u'Acessos Biometricos'


    def get_absolute_url(self):
        return '/systi/acesso_biometrico/{}/'.format(self.id)

    def __str__(self):
        return self.id_usuario_fechadura



class Transferencia(ModelPlus):
    motivo_transferencia = models.CharFieldPlus(
        verbose_name=u'Motivo da Transferência',
        max_length=30,
        choices=SysTIChoices.TIPOS_SOLICITACAO.items(),
        default=SysTIChoices.CHAMADO
    )
    anexo_motivo = models.FileField(upload_to='systi/anexosMotivos/', verbose_name=u'Anexo do Motivo')
    descricao = models.TextField(verbose_name=u'Descrição', max_length=225)
    setor_origem = models.ForeignKeyPlus('comum.Sala', verbose_name=u'Setor de Origem', related_name='sala_origem', blank=True, null=True)
    setor_destino = models.ForeignKeyPlus('comum.Sala', verbose_name=u'Setor de Destino', related_name='sala_destino')
    ativos_transferidos = models.ManyToManyFieldPlus(Ativo, verbose_name=u'Ativos a Serem Transferidos')
    termo_recebimento = models.FileField(upload_to='systi/anexosTermosRecebimentos/', verbose_name=u'Anexo do Termo de Recebimento')
    data_solicitacao = models.DateFieldPlus(verbose_name=u'Data da Solicitação')
    altorizada = models.CharFieldPlus(
        verbose_name=u'Altorizada',
        max_length=30,
        null=True,
        blank=True,
        choices=SysTIChoices.TRANSFERENCIA_ALTORIZACAO.items(),
        default=SysTIChoices.AGUARDANDO_ALTORIZACAO
    )
    transferida = models.CharFieldPlus(
        verbose_name=u'Transferida',
        max_length=30,
        null=True,
        blank=True,
        choices=SysTIChoices.TRANSFERENCIAS.items(),
        default=SysTIChoices.AGUARDANDO_ALTORIZACAO
    )
    data_altorizada = models.DateFieldPlus(verbose_name=u'Data que foi Altorizada', null=True, blank=True)
    data_transferencia = models.DateFieldPlus(verbose_name=u'Data da Transferencia', null=True, blank=True)


    anexo_motivo.help_text = help_text = HELP_TEXT = u'Será aceito arquivo com tamanho máximo 3MB e que seja do tipo: ' + \
                                                     u', '.join(DOCUMENT_EXTENSIONS + IMAGE_EXTENSIONS[0:-1]) + ' ou ' + \
                                                     IMAGE_EXTENSIONS[-1] + '.'
    termo_recebimento.help_text = help_text = HELP_TEXT = u'Será aceito arquivo com tamanho máximo 3MB e que seja do tipo: ' + \
                                                     u', '.join(DOCUMENT_EXTENSIONS + IMAGE_EXTENSIONS[0:-1]) + ' ou ' + \
                                                     IMAGE_EXTENSIONS[-1] + '.'

    class Meta:
        verbose_name = u'Transferência'
        verbose_name_plural = u'Transferências'

    def get_absolute_url(self):
        return '/systi/transferencia/{}/'.format(self.id)


class Material(ModelPlus):
    nome_material = models.CharFieldPlus(verbose_name=u'Nome do Material', max_length=30)
    tipo_material = models.CharFieldPlus(verbose_name=u'Tipo do Material', max_length=20)
    local_guardado = models.ForeignKeyPlus('systi.Compartimento', verbose_name='Local Guardado')
    descricao = models.TextField(verbose_name=u'Descrição', max_length=30)
    unidade_de_medida = models.CharFieldPlus(verbose_name=u'Unidade de Medida', max_length=25, choices=UNIDADE_MEDIDA.items(), default=UNIDADE_MEDIDA.get('Und'))
    quantidade = models.CharFieldPlus(verbose_name=u'Quantidade', max_length=30)
    fornecedor = models.ForeignKeyPlus('systi.Fornecedor', verbose_name='Fornecedor')

    class Meta:
        verbose_name = u'Material'
        verbose_name_plural = u'Materiais'

    def get_absolute_url(self):
        return '/systi/material/{}/'.format(self.id)

    def __str__(self):
        return self.nome_material

class Compartimento(ModelPlus):
    codigo_compartimento = models.CharFieldPlus(verbose_name=u'Código', max_length=30)
    nome = models.CharFieldPlus(verbose_name=u'Nome', max_length=30)
    pai = models.ForeignKeyPlus('systi.Compartimento', verbose_name='Compartimento Pai', help_text='Ex.: Este compartimento está dentro que qual outro compartimento?', blank=True, null=True)

    class Meta:
        verbose_name = u'Compartimento'
        verbose_name_plural = u'Compartimentos'

    def get_absolute_url(self):
        return '/systi/compartimento/{}/'.format(self.id)

    def __str__(self):
        return self.nome

class Emprestimo(ModelPlus):
    ativo = models.ForeignKeyPlus('systi.Ativo', verbose_name='Ativos')
    motivo = models.TextField(verbose_name=u'Justificativa', max_length=40)
    data_emprestimo = models.DateFieldPlus(u'Data do Empréstimo')
    data_devolucao = models.DateFieldPlus(u'Data de Devolução')
    estado = models.CharFieldPlus(verbose_name=u'Estado do Empréstimo', max_length=25, choices=SysTIChoices.ESTADO_EMPRESTIMOS.items(), default=SysTIChoices.EM_ABERTO)
    setor_origem = models.ForeignKeyPlus('comum.Sala', verbose_name='Setor de Origem', related_name='setor_origem')
    setor_destino = models.ForeignKeyPlus('comum.Sala', verbose_name='Setor de Destino', related_name='setor_destino')

    class Meta:
        verbose_name = u'Empréstimo'
        verbose_name_plural = u'Empréstimos'

    def get_absolute_url(self):
        return '/systi/emprestimo/{}/'.format(self.id)

    def __str__(self):
        return self.data_emprestimo

class Servico(ModelPlus):

    class Meta:
        abstract = True

    motivo_servico= models.CharFieldPlus(
        verbose_name=u'Motivo do Serviço',
        max_length=30,
        choices=SysTIChoices.TIPOS_SOLICITACAO.items(),
        default=SysTIChoices.CHAMADO
    )
    chamado = models.ForeignKeyPlus('centralservicos.Chamado', verbose_name=u'Chamado' ,blank=True, null=True)
    anexo_motivo = models.FileField(upload_to='systi/anexosMotivos/', verbose_name=u'Anexo do Motivo', blank=True, null=True)
    equipamentos_enviados = models.ManyToManyFieldPlus(Ativo, verbose_name=u'Equipamentos a serem Consertados')
    data_diagnostico = models.DateFieldPlus(u'Data do Diagnóstico')
    diagnostico = models.TextField(verbose_name=u'Defeitos Apresentados', max_length=300)
    tipo_servico = models.CharFieldPlus(verbose_name=u'Tipo do Serviço', max_length=25, choices=TIPO_SERVICO.items(), default=TIPO_SERVICO.get('Manutenção'))
    estado_servico = models.CharFieldPlus(verbose_name=u'Estado', max_length=25, choices=SysTIChoices.ESTADOS_SERVICO.items(), default=SysTIChoices.AGUARDANDO_DIAGNOSTICO, blank=True, null=True)
    ordem_servico = models.CharFieldPlus(verbose_name='Número da Ordem do Serviço', max_length=25)
    motivo_cancel_ou_suspen = models.TextField(verbose_name='Motivo da Suspenção ou Cacelamento', blank=True, null=True)


class ServicoInterno(Servico):
    procedimentos_realizados = models.TextField(verbose_name='Procedimentos a Serem Realizados', max_length=300, null=True, blank=True)
    materiais_utilizados = models.ManyToManyFieldPlus('systi.Material', verbose_name='Materiais Utilizados', blank=True, null=True)
    data_realizacao = models.DateFieldPlus(u'Data da Realização', null=True, blank=True)
    data_prevista_conclusao = models.DateFieldPlus(u'Data Prevista da Conclusão')
    data_conclusao = models.DateFieldPlus(u'Data da Conclusão', blank=True, null=True)


    class Meta:
        verbose_name = u'Serviço Interno'
        verbose_name_plural = u'Serviços Internos'

    def get_absolute_url(self):
        return '/systi/servicointerno/{}/'.format(self.id)

    def __str__(self):
        return self.ordem_servico

class ServicoExterno(Servico):
    data_do_envio = models.DateFieldPlus(u'Data do Envio', blank=True, null=True)
    data_prevista_devolucao = models.DateFieldPlus(u'Data Prevista da Devolução', blank=True, null=True)
    anexo_nota_fiscal_recibo = models.FileField(upload_to='systi/anexoNotasFiscaisOuRecibos/', verbose_name='Anexar Nota Fiscal ou Recibo', blank=True, null=True)
    anexo_termo = models.FileField(upload_to='systi/anexoTermosServico/', verbose_name='Anexar Termo', blank=True, null=True)
    prestador = models.ForeignKeyPlus('systi.Fornecedor', verbose_name='Selecionar Prestador', blank=True, null=True)
    parecer = models.CharFieldPlus(verbose_name='Parecer', blank=True, null=True)

    class Meta:
        verbose_name = u'Serviço Externo'
        verbose_name_plural = u'Serviços Externos'

    def get_absolute_url(self):
        return '/systi/servicoexterno/{}/'.format(self.id)

    def __str__(self):
        return self.ordem_servico


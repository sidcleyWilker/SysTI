# -*- coding: utf-8 -*-
from pygments.lexer import default

from djtools.db import models
from djtools.models import ModelPlus

stados_do_usuario = {
    'Ativo': 'Ativo',
    'Inativo': 'Inativo'
}

TIPO_USUARIO = {
    'Servidor': 'Servidor',
    'Aluno': 'Aluno'
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


class Categoria(ModelPlus):
    nome = models.CharFieldPlus(verbose_name=u'Nome da Categoria', max_length=30, help_text=u'Ex: Hardware, Software, Rede ...')
    descricao = models.CharFieldPlus(verbose_name=u'Descrição', max_length=30)
    ativo = models.OneToOneFieldPlus('systi.Ativo', blank=True, null=True)

    class Meta:
        verbose_name = u'Categoria'
        verbose_name_plural = u'Categorias'

    def __str__(self):
        return self.nome


class CategoriaHardware(Categoria):
    fabricante = models.CharFieldPlus(verbose_name=u'Fabricante', max_length=30)
    versao = models.DecimalFieldPlus(verbose_name=u'Versão do modelo')

    class Meta:
        verbose_name = u'Categoria do Hardware'
        verbose_name_plural = u'Categoria dos Hardwares'


class CategoriaRede(Categoria):
    fabricante = models.CharFieldPlus(verbose_name=u'Fabricante', max_length=30)
    versao = models.DecimalFieldPlus(verbose_name=u'Versão do modelo')
    numero_portas = models.IntegerFieldPlus(verbose_name=u'Quantidade de Portas do Ativo')

    class Meta:
        verbose_name = u'Categoria de Rede'
        verbose_name_plural = u'Categoria dos Ativos de Rede'

class CategoriaSoftware(Categoria):
    nome_software = models.CharFieldPlus(verbose_name=u'Nome do Software', max_length=30)
    versao_software = models.DecimalFieldPlus(verbose_name=u'Versão do Software')
    pago = models.CharFieldPlus(verbose_name=u'Foi Comprado ?', default=False)

    class Meta:
        verbose_name = u'Categoria do Software'
        verbose_name_plural = u'Categoria dos Ativos de Softwares'

class Ativo(ModelPlus):
    #categorias = {'Software': 'Software', 'Rede':'Rede', 'Hardware':'Hardware'}
    nome = models.CharFieldPlus(verbose_name=u'Nome do Ativo', max_length=30)
    tombamento = models.CharFieldPlus(verbose_name=u'Numero de Tombamento', max_length=30)
    numero_etiqueta = models.CharFieldPlus(verbose_name=u'Numero da Etiqueta', max_length=30)
    numero_serie = models.CharFieldPlus(verbose_name=u'Numero da Serie', max_length=30)
    numero_produto = models.CharFieldPlus(verbose_name=u'Numero do Produto', max_length=30)
    fornecedor = models.ForeignKeyPlus('systi.Fornecedor',verbose_name=u'Fornecedor')
    local_do_ativo = models.ForeignKeyPlus('comum.Sala', verbose_name=u'Local do Ativo')
    #categoria = models.CharFieldPlus(verbose_name=u'Categoria', max_length=30, choices=categorias.items())


    class Meta:
        verbose_name = u'Ativo'
        verbose_name_plural = u'Ativos'


    def get_absolute_url(self):
        return '/systi/ativo/{}/'.format(self.id)

    def __str__(self):
        return self.nome



class Atributo(ModelPlus):
    nome_atributo = models.CharFieldPlus(verbose_name=u'Nome do Atributo', max_length=30)
    nome_campo = models.CharFieldPlus(verbose_name=u'Nome do Campo', max_length=30)
    tipo_campo = models.CharFieldPlus(verbose_name=u'Tipo do campo', max_length=30)
    is_nulo = models.BooleanField(verbose_name=u'Pode ser nulo', default=False)
    unico = models.BooleanField(verbose_name=u'È unico', default=False)

class ValorAtt(ModelPlus):
    valor = models.CharFieldPlus(verbose_name=u'Valor', max_length=50)
    id_atributo = models.ForeignKeyPlus(Atributo, verbose_name=u'Atributo')


class AcessoBiometrico(ModelPlus):
    id_usuario_fechadura = models.CharFieldPlus(verbose_name=u'Identificação Usuário Fechadura', max_length=40)
    data_registro = models.DateFieldPlus(verbose_name=u'Data do Registro')
    data_des_registro = models.DateFieldPlus(u'Data do des-registro', blank=True, null=True)
    local_da_fechadura = models.ForeignKeyPlus('comum.Sala', verbose_name=u'Local do Fechadura')
    tipo_do_usuario = models.CharFieldPlus(verbose_name=u'Tipo do Usuário', max_length=10, choices=TIPO_USUARIO.items(), default=TIPO_USUARIO.get('Aluno'))
    aluno = models.ForeignKeyPlus('edu.Aluno', verbose_name=u'Aluno', blank=True, null=True)
    servidor = models.ForeignKeyPlus('rh.Servidor', verbose_name=u'Servidor do IF', blank=True, null=True)

    class Meta:
        verbose_name = u'Acesso Biometrico'
        verbose_name_plural = u'Acessos Biometricos'


    def get_absolute_url(self):
        return '/systi/acessobiometrico/{}/'.format(self.id)

    def __str__(self):
        return self.id_usuario_fechadura
# -*- coding: utf-8 -*-

from djtools.db import models
from djtools.models import ModelPlus

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


class ValorAtt(models.Model):
    att = models.ForeignKey(Atributo)
    modelo = models.ForeignKey(Ativo)
    valor = models.CharField(max_length=30)


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

class Material(ModelPlus):
    nome_material = models.CharFieldPlus(verbose_name=u'Nome do Material', max_length=30)
    tipo_material = models.CharFieldPlus(verbose_name=u'Tipo do Material', max_length=20)
    #local_guardado = models.ForeignKeyPlus('systi.Compartimento', verbose_name='Local Guardado')
    local_guardado = models.CharFieldPlus(verbose_name=u'Local Guardado', max_length=30)
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
    nome = models.CharFieldPlus(verbose_name=u'Nome do Material', max_length=30)
    descricao = models.TextField(verbose_name=u'Descrição', max_length=30)
    class Meta:
        verbose_name = u'Compartimento'
        verbose_name_plural = u'Compartimentos'

    def get_absolute_url(self):
        return '/systi/compartimento/{}/'.format(self.id)

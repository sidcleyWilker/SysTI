
import unittest
from systi.models import Fornecedor, Categoria, CategoriaHardware, \
    CategoriaRede, CategoriaSoftware, Ativo, Atributo

#Classe de testes unitarios
class SysTiTestCase(unittest.TestCase):

    def setUp(self):

        # cadastra fornecedor e testa o código
        self.fornecedor = Fornecedor.objects.create(
            nome      = 'João da Silva',
            cpf       = '326.664.671-12',
            cnpj      = '31.102.644/0001-14',
            telefone1 = '(83) 99999-9999',
            telefone2 = '(83) 88888-8888',
            email     = 'josedasilva@gmail.com'
            )
        self.fornecedorNomeTest()

        #Cadastra Categoria e testa o código
        self.categoria = Categoria.objects.create(
            nome      = 'Generica',
            descricao = 'Descrição da Categoria',
            ativo     = None,
            )
        self.categoriaTest()

        #Cadastra CategoriaHardware e testa o código
        self.categoriaHardware = CategoriaHardware.objects.create(
                nome      = 'Hardware',
                descricao = 'Descrição da Categoria',
                ativo     = None,
                fabricante = 'INTEL',
                versao     = '1.0',
                )
        self.categoriaHardwareTest()

        #Cadastra CategoriaRede e testa o código
        self.categoriaRede = CategoriaRede.objects.create(
                nome      = 'Hardware',
                descricao = 'Descrição da Categoria',
                ativo     = None,
                fabricante    = 'INTELBRAZ',
                versao        = '2.0',
                numero_portas = '8080',)
        self.categoriaRedeTest()

        #Cadastra CategoriaSoftware e testa o código
        self.categoriaSoftware = CategoriaSoftware.objects.create(
                nome      = 'Hardware',
                descricao = 'Descrição da Categoria',
                ativo     = None,
                nome_software   = 'SySTI',
                versao_software = '1.0',
                pago            = False,
                )
        self.categoriaSoftwareTest()

        #Cadastra Atributo e testa o código
        self.atributo = Atributo.objects.create(
                nome_atributo = 'Roteador',
                nome_campo    = 'Roteador',
                tipo_campo    = 'Hardware',
                is_nulo       = False,
                unico         = True,
        )
        self.atributoTest()

        #Cadastra Ativo e testa o código
        self.ativo = Ativo.objects.create(
            nome =            'Computador',
            tombamento =      '68945042',
            numero_etiqueta = '86646',
            numero_serie =    '6757763',
            numero_produto =  '66462',
            fornecedor =      None,
            local_do_ativo =  None,
        )
        self.ativoTest()


    #Testes de cadastro de Fornecedor
    def fornecedorNomeTest(self):
        self.assertEquals(self.fornecedor.nome, 'João da Silva')

    def categoriaTest(self):
        self.assertEquals(self.categoria.nome, 'Generica')
    #Teste de cadastro de Categoria generica

    #Teste de cadastro de Categoria de Hardware
    def categoriaHardwareTest(self):
        self.assertEquals(self.categoriaHardware.nome, 'Hardware')

    #Teste de cadastro de Categoria de Rede
    def categoriaRedeTest(self):
        self.assertEquals(self.categoriaRede.nome, 'Hardware')

    #Teste de cadastro de Categoria de Software
    def categoriaSoftwareTest(self):
        self.assertEquals(self.categoriaSoftware.nome, 'Hardware')

    #Teste de cadastro de Categoria de Software
    def atributoTest(self):
        self.assertEquals(self.atributo.nome, 'Roteador')

    #Teste de cadastro de Categoria de Software
    def ativoTest(self):
        self.assertEquals(self.atributo.nome, 'Computador')

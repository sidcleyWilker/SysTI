# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import djtools.dbfields


class Migration(migrations.Migration):

    dependencies = [
        ('comum', '0003_auto_20160122_0804'),
        ('edu', '0036_auto_20161120_1500'),
        ('rh', '0020_auto_20151017_1559'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcessoBiometrico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_usuario_fechadura', djtools.dbfields.CharFieldPlus(max_length=40, verbose_name='Identifica\xe7\xe3o Na Fechadura')),
                ('data_registro', djtools.dbfields.DateFieldPlus(max_length=255, null=True, verbose_name='Data do Registro', blank=True)),
                ('data_des_registro', djtools.dbfields.DateFieldPlus(max_length=255, null=True, verbose_name='Data do des-registro', blank=True)),
                ('tipo_do_usuario', djtools.dbfields.CharFieldPlus(default=b'Aluno', max_length=25, verbose_name='Tipo do Usu\xe1rio', choices=[(b'Aluno', b'Aluno'), (b'Servidor', b'Servidor'), (b'Servidor Terceirizado', b'Servidor Terceirizado')])),
                ('servidor_terceirizado', djtools.dbfields.CharFieldPlus(max_length=255, null=True, verbose_name='Nome do Servidor ou Visitante', blank=True)),
                ('aluno', djtools.dbfields.ForeignKeyPlus(verbose_name='Aluno', blank=True, to='edu.Aluno', null=True)),
                ('local_da_fechadura', djtools.dbfields.ForeignKeyPlus(verbose_name='Local do Fechadura', to='comum.Sala')),
                ('servidor', djtools.dbfields.ForeignKeyPlus(verbose_name='Servidor do IF', blank=True, to='rh.Servidor', null=True)),
            ],
            options={
                'verbose_name': 'Acesso Biometrico',
                'verbose_name_plural': 'Acessos Biometricos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ativo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', djtools.dbfields.CharFieldPlus(max_length=30, verbose_name='Nome do Ativo')),
                ('tombamento', djtools.dbfields.CharFieldPlus(max_length=30, verbose_name='Numero de Tombamento')),
                ('numero_etiqueta', djtools.dbfields.CharFieldPlus(max_length=30, verbose_name='Numero da Etiqueta')),
                ('numero_serie', djtools.dbfields.CharFieldPlus(max_length=30, verbose_name='Numero da Serie')),
                ('numero_produto', djtools.dbfields.CharFieldPlus(max_length=30, verbose_name='Numero do Produto')),
            ],
            options={
                'verbose_name': 'Ativo',
                'verbose_name_plural': 'Ativos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Atributo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome_campo', djtools.dbfields.CharFieldPlus(max_length=30, verbose_name='Nome do Campo')),
                ('tipo_campo', djtools.dbfields.CharFieldPlus(default=b'Texto', max_length=30, verbose_name='Tipo do campo', choices=[(b'Float', b'Float'), (b'Data', b'Data'), (b'Texto', b'Texto'), (b'Inteiro', b'Inteiro')])),
                ('obrigatorio', models.BooleanField(default=False, verbose_name='Obrigatorio')),
                ('unico', models.BooleanField(default=False, verbose_name='\xc8 unico')),
                ('valor', models.CharField(max_length=50, verbose_name='Valor')),
            ],
            options={
                'verbose_name': 'Campo Adicional',
                'verbose_name_plural': 'Campos Adicionais',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', djtools.dbfields.CharFieldPlus(help_text='Ex: Hardware, Software, Rede ...', max_length=30, verbose_name='Nome da Categoria')),
                ('descricao', models.TextField(max_length=30, verbose_name='Descri\xe7\xe3o')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Compartimento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', djtools.dbfields.CharFieldPlus(max_length=30, verbose_name='Nome do Compartimento')),
                ('descricao', djtools.dbfields.CharFieldPlus(max_length=30, verbose_name='Descri\xe7\xe3o')),
            ],
            options={
                'verbose_name': 'Compartimento',
                'verbose_name_plural': 'Compartimentos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('motivo', models.TextField(max_length=40, verbose_name='Justificativa')),
                ('data_emprestimo', djtools.dbfields.DateFieldPlus(max_length=255, null=True, verbose_name='Data do Emprestimo', blank=True)),
                ('data_devolucao', djtools.dbfields.DateFieldPlus(max_length=255, null=True, verbose_name='Data de Devolu\xe7\xe3o', blank=True)),
                ('estado', djtools.dbfields.CharFieldPlus(default=None, max_length=25, verbose_name='Estado do Emprestimo', choices=[(b'Cancelado', b'Cancelado'), (b'Aberto', b'Aberto')])),
                ('ativo', djtools.dbfields.ForeignKeyPlus(verbose_name=b'Ativos', to='systi.Ativo')),
                ('setor_destino', djtools.dbfields.ForeignKeyPlus(related_name='setor_destino', verbose_name=b'Setor de Destino', to='comum.Sala')),
                ('setor_origem', djtools.dbfields.ForeignKeyPlus(related_name='setor_origem', verbose_name=b'Setor de Origem', to='comum.Sala')),
            ],
            options={
                'verbose_name': 'Emprestimo',
                'verbose_name_plural': 'Emprestimos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', djtools.dbfields.CharFieldPlus(max_length=30, verbose_name='Nome do Fornecedor')),
                ('cpf', djtools.dbfields.BrCpfField(max_length=14, null=True, verbose_name='CPF', blank=True)),
                ('cnpj', djtools.dbfields.BrCnpjField(max_length=18, null=True, verbose_name='CNPJ', blank=True)),
                ('telefone1', djtools.dbfields.BrTelefoneField(max_length=14, verbose_name='Telefone para Contato')),
                ('telefone2', djtools.dbfields.BrTelefoneField(max_length=14, null=True, verbose_name='Telefone para Contato Reserva', blank=True)),
                ('email', models.EmailField(max_length=75, verbose_name='E-mail para Contato')),
            ],
            options={
                'verbose_name': 'Fornecedor',
                'verbose_name_plural': 'Fornecedores',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome_material', djtools.dbfields.CharFieldPlus(max_length=30, verbose_name='Nome do Material')),
                ('tipo_material', djtools.dbfields.CharFieldPlus(max_length=20, verbose_name='Tipo do Material')),
                ('descricao', models.TextField(max_length=30, verbose_name='Descri\xe7\xe3o')),
                ('unidade_de_medida', djtools.dbfields.CharFieldPlus(default=b'Unidade', max_length=25, verbose_name='Unidade de Medida', choices=[(b'Cm', b'Centimetro'), (b'Pc', b'Pacote'), (b'Mt', b'Metro'), (b'Lt', b'Litro'), (b'Cx', b'Caixa'), (b'Und', b'Unidade')])),
                ('quantidade', djtools.dbfields.CharFieldPlus(max_length=30, verbose_name='Quantidade')),
                ('fornecedor', djtools.dbfields.ForeignKeyPlus(verbose_name=b'Fornecedor', to='systi.Fornecedor')),
                ('local_guardado', djtools.dbfields.ForeignKeyPlus(verbose_name=b'Local Guardado', to='systi.Compartimento')),
            ],
            options={
                'verbose_name': 'Material',
                'verbose_name_plural': 'Materiais',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Transferencia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('motivo_transferencia', djtools.dbfields.CharFieldPlus(default='Chamdo', max_length=30, verbose_name='Motivo da Transferencia', choices=[('E-mail', 'E-mail'), ('Chamdo', 'Chamdo'), ('Memorando', 'Memorando')])),
                ('anexo_motivo', models.FileField(help_text='Ser\xe1 aceito arquivo com tamanho m\xe1ximo 3MB e que seja do tipo: pdf, txt, doc, dot, docx, odt, bmp, jpeg, jpg ou png.', upload_to=b'systi/anexosMotivos/', verbose_name='Anexo do Motivo')),
                ('descricao', models.TextField(max_length=225, verbose_name='Descri\xe7\xe3o')),
                ('termo_recebimento', models.FileField(help_text='Ser\xe1 aceito arquivo com tamanho m\xe1ximo 3MB e que seja do tipo: pdf, txt, doc, dot, docx, odt, bmp, jpeg, jpg ou png.', upload_to=b'systi/anexosTermosRecebimentos/', verbose_name='Anexo do Termo de Recebimento')),
                ('data_solicitacao', djtools.dbfields.DateFieldPlus(max_length=255, verbose_name='Data da Solicita\xe7\xe3o')),
                ('altorizada', djtools.dbfields.CharFieldPlus(default='Aguardando Altoriza\xe7\xe3o', choices=[('Altorizado(a)', 'Altorizado(a)'), ('Aguardando Altoriza\xe7\xe3o', 'Aguardando Altoriza\xe7\xe3o')], max_length=30, blank=True, null=True, verbose_name='Altorizada')),
                ('transferida', djtools.dbfields.CharFieldPlus(default='Aguardando Altoriza\xe7\xe3o', choices=[('Transferida(o)', 'Transferida(o)'), ('Aguardando Altoriza\xe7\xe3o', 'Aguardando Altoriza\xe7\xe3o'), ('Aguardando Transferencia', 'Aguardando Transferencia')], max_length=30, blank=True, null=True, verbose_name='Transferida')),
                ('data_altorizada', djtools.dbfields.DateFieldPlus(max_length=255, null=True, verbose_name='Data que foi Altorizada', blank=True)),
                ('data_transferencia', djtools.dbfields.DateFieldPlus(max_length=255, null=True, verbose_name='Data da Transferencia', blank=True)),
                ('ativos_transferidos', djtools.dbfields.ManyToManyFieldPlus(to='systi.Ativo', verbose_name='Ativos a Serem Transferidos')),
                ('setor_destino', djtools.dbfields.ForeignKeyPlus(related_name='sala_destino', verbose_name='Setor de Destino', to='comum.Sala')),
                ('setor_origem', djtools.dbfields.ForeignKeyPlus(related_name='sala_origem', verbose_name='Setor de Origem', blank=True, to='comum.Sala', null=True)),
            ],
            options={
                'verbose_name': 'Transferencia',
                'verbose_name_plural': 'Transferencias',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='atributo',
            name='categoria_instancia',
            field=models.ForeignKey(verbose_name='Instancia', to='systi.Categoria'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ativo',
            name='categoria_do_ativo',
            field=models.ForeignKey(verbose_name='Categoria', to='systi.Categoria'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ativo',
            name='fornecedor',
            field=djtools.dbfields.ForeignKeyPlus(verbose_name='Fornecedor', to='systi.Fornecedor'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ativo',
            name='local_do_ativo',
            field=djtools.dbfields.ForeignKeyPlus(verbose_name='Local do Ativo', to='comum.Sala'),
            preserve_default=True,
        ),
    ]

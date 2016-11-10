# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import djtools.dbfields


class Migration(migrations.Migration):

    dependencies = [
        ('comum', '0003_auto_20160122_0804'),
    ]

    operations = [
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
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', djtools.dbfields.CharFieldPlus(help_text='Ex: Hardware, Software, Rede ...', max_length=30, verbose_name='Nome da Categoria')),
                ('descricao', djtools.dbfields.CharFieldPlus(max_length=30, verbose_name='Descri\xe7\xe3o')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CategoriaHardware',
            fields=[
                ('categoria_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='systi.Categoria')),
                ('fabricante', djtools.dbfields.CharFieldPlus(max_length=30, verbose_name='Fabricante')),
                ('versao', djtools.dbfields.DecimalFieldPlus(verbose_name='Vers\xe3o do modelo', max_digits=12, decimal_places=2)),
            ],
            options={
                'verbose_name': 'Categoria do Hardware',
                'verbose_name_plural': 'Categoria dos Hardwares',
            },
            bases=('systi.categoria',),
        ),
        migrations.CreateModel(
            name='CategoriaRede',
            fields=[
                ('categoria_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='systi.Categoria')),
                ('fabricante', djtools.dbfields.CharFieldPlus(max_length=30, verbose_name='Fabricante')),
                ('versao', djtools.dbfields.DecimalFieldPlus(verbose_name='Vers\xe3o do modelo', max_digits=12, decimal_places=2)),
                ('numero_portas', djtools.dbfields.IntegerFieldPlus(verbose_name='Quantidade de Portas do Ativo')),
            ],
            options={
                'verbose_name': 'Categoria de Rede',
                'verbose_name_plural': 'Categoria dos Ativos de Rede',
            },
            bases=('systi.categoria',),
        ),
        migrations.CreateModel(
            name='CategoriaSoftware',
            fields=[
                ('categoria_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='systi.Categoria')),
                ('nome_software', djtools.dbfields.CharFieldPlus(max_length=30, verbose_name='Nome do Software')),
                ('versao_software', djtools.dbfields.DecimalFieldPlus(verbose_name='Vers\xe3o do Software', max_digits=12, decimal_places=2)),
                ('pago', djtools.dbfields.CharFieldPlus(default=False, max_length=255, verbose_name='Foi Comprado ?')),
            ],
            options={
                'verbose_name': 'Categoria do Software',
                'verbose_name_plural': 'Categoria dos Ativos de Softwares',
            },
            bases=('systi.categoria',),
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
        migrations.AddField(
            model_name='categoria',
            name='ativo',
            field=djtools.dbfields.ForeignKeyPlus(to='systi.Ativo'),
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

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import djtools.dbfields


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0036_auto_20161008_1832'),
        ('comum', '0003_auto_20160122_0804'),
        ('rh', '0020_auto_20151017_1559'),
        ('systi', '0002_auto_20161101_2035'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcessoBiometrico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_usuario_fechadura', djtools.dbfields.CharFieldPlus(max_length=40, verbose_name='Identifica\xe7\xe3o Usu\xe1rio Fechadura')),
                ('data_registro', djtools.dbfields.DateFieldPlus(auto_now_add=True, verbose_name='Data do Registro', max_length=255)),
                ('data_des_registro', djtools.dbfields.DateFieldPlus(max_length=255, null=True, verbose_name='Data do des-registro', blank=True)),
                ('tipo_do_usuario', djtools.dbfields.CharFieldPlus(max_length=10, verbose_name='Tipo do Usu\xe1rio', choices=[(b'Ativo', b'Ativo'), (b'Inativo', b'Inativo')])),
                ('aluno', djtools.dbfields.ForeignKeyPlus(verbose_name='Aluno', to='edu.Aluno')),
                ('local_da_fechadura', djtools.dbfields.ForeignKeyPlus(verbose_name='Local do Fechadura', to='comum.Sala')),
                ('servidor', djtools.dbfields.ForeignKeyPlus(verbose_name='Servidor do IF', to='rh.Servidor')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Atributo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome_atributo', djtools.dbfields.CharFieldPlus(max_length=30, verbose_name='Nome do Atributo')),
                ('nome_campo', djtools.dbfields.CharFieldPlus(max_length=30, verbose_name='Nome do Campo')),
                ('tipo_campo', djtools.dbfields.CharFieldPlus(max_length=30, verbose_name='Tipo do campo')),
                ('is_nulo', models.BooleanField(default=False, verbose_name='Pode ser nulo')),
                ('unico', models.BooleanField(default=False, verbose_name='\xc8 unico')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ValorAtt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('valor', djtools.dbfields.CharFieldPlus(max_length=50, verbose_name='Valor')),
                ('id_atributo', djtools.dbfields.ForeignKeyPlus(verbose_name='Atributo', to='systi.Atributo')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]

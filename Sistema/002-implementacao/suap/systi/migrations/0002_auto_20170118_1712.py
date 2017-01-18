# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import djtools.dbfields


class Migration(migrations.Migration):

    dependencies = [
        ('systi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicoexterno',
            name='estado_servico',
            field=djtools.dbfields.CharFieldPlus(default=('Aguardando Diagn\xf3stico',), max_length=25, verbose_name='Estado', choices=[(('Em Execu\xe7\xe3o',), 'Em Execu\xe7\xe3o'), (('Cacelado',), 'Cancelado'), (('Aguardando Diagn\xf3stico',), 'Aguardando Diagn\xf3stico'), (('Suspenso',), 'Suspenso'), (('Recolhido',), 'Recolhido'), (('Devolvido',), 'Devolvido')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='servicoexterno',
            name='motivo_servico',
            field=djtools.dbfields.CharFieldPlus(default='Chamado', max_length=30, verbose_name='Motivo do Servi\xe7o', choices=[('E-mail', 'E-mail'), ('Chamado', 'Chamado'), ('Memorando', 'Memorando')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='servicointerno',
            name='data_realizacao',
            field=djtools.dbfields.DateFieldPlus(max_length=255, null=True, verbose_name='Data da Realiza\xe7\xe3o', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='servicointerno',
            name='estado_servico',
            field=djtools.dbfields.CharFieldPlus(default=('Aguardando Diagn\xf3stico',), max_length=25, verbose_name='Estado', choices=[(('Em Execu\xe7\xe3o',), 'Em Execu\xe7\xe3o'), (('Cacelado',), 'Cancelado'), (('Aguardando Diagn\xf3stico',), 'Aguardando Diagn\xf3stico'), (('Suspenso',), 'Suspenso'), (('Recolhido',), 'Recolhido'), (('Devolvido',), 'Devolvido')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='servicointerno',
            name='motivo_servico',
            field=djtools.dbfields.CharFieldPlus(default='Chamado', max_length=30, verbose_name='Motivo do Servi\xe7o', choices=[('E-mail', 'E-mail'), ('Chamado', 'Chamado'), ('Memorando', 'Memorando')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='servicointerno',
            name='procedimentos_realizados',
            field=models.TextField(max_length=300, null=True, verbose_name=b'Procedimentos a Serem Realizados', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='transferencia',
            name='motivo_transferencia',
            field=djtools.dbfields.CharFieldPlus(default='Chamado', max_length=30, verbose_name='Motivo da Transfer\xeancia', choices=[('E-mail', 'E-mail'), ('Chamado', 'Chamado'), ('Memorando', 'Memorando')]),
            preserve_default=True,
        ),
    ]

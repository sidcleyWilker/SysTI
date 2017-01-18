# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import djtools.dbfields


class Migration(migrations.Migration):

    dependencies = [
        ('systi', '0002_auto_20170118_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='estado',
            field=djtools.dbfields.CharFieldPlus(default=('Em Aberto',), max_length=25, verbose_name='Estado do Empr\xe9stimo', choices=[(('Em Aberto',), 'Em Aberto'), (('Pendente',), 'Pendente'), (('Vigente',), 'Vigente'), (('Devolvido',), 'Devolvido'), (('Aguardando Termo',), 'Aguardando Termo'), (('Solicitado',), 'Solicitado')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='servicoexterno',
            name='estado_servico',
            field=djtools.dbfields.CharFieldPlus(default=('Aguardando Diagn\xf3stico',), choices=[(('Em Execu\xe7\xe3o',), 'Em Execu\xe7\xe3o'), (('Cacelado',), 'Cancelado'), (('Aguardando Diagn\xf3stico',), 'Aguardando Diagn\xf3stico'), (('Suspenso',), 'Suspenso'), (('Recolhido',), 'Recolhido'), (('Devolvido',), 'Devolvido')], max_length=25, blank=True, null=True, verbose_name='Estado'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='servicointerno',
            name='estado_servico',
            field=djtools.dbfields.CharFieldPlus(default=('Aguardando Diagn\xf3stico',), choices=[(('Em Execu\xe7\xe3o',), 'Em Execu\xe7\xe3o'), (('Cacelado',), 'Cancelado'), (('Aguardando Diagn\xf3stico',), 'Aguardando Diagn\xf3stico'), (('Suspenso',), 'Suspenso'), (('Recolhido',), 'Recolhido'), (('Devolvido',), 'Devolvido')], max_length=25, blank=True, null=True, verbose_name='Estado'),
            preserve_default=True,
        ),
    ]

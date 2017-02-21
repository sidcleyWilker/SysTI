# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import djtools.dbfields


class Migration(migrations.Migration):

    dependencies = [
        ('centralservicos', '0026_auto_20150727_1704'),
        ('systi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transferencia',
            name='chamado',
            field=djtools.dbfields.ForeignKeyPlus(verbose_name='Chamado', blank=True, to='centralservicos.Chamado', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='compartimento',
            name='descricao',
            field=djtools.dbfields.CharFieldPlus(max_length=30, verbose_name='Descri\xe7\xe3o'),
            preserve_default=True,
        ),
    ]

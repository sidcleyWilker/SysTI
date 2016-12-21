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
            model_name='emprestimo',
            name='data_devolucao',
            field=djtools.dbfields.DateFieldPlus(max_length=255, verbose_name='Data de Devolu\xe7\xe3o'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='data_emprestimo',
            field=djtools.dbfields.DateFieldPlus(max_length=255, verbose_name='Data do Empr\xe9stimo'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='estado',
            field=djtools.dbfields.CharFieldPlus(default=None, max_length=25, verbose_name='Estado do Empr\xe9stimo', choices=[(b'Cancelado', b'Cancelado'), (b'Aberto', b'Aberto')]),
            preserve_default=True,
        ),
    ]

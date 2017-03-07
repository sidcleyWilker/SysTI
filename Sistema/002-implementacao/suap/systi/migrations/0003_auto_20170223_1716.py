# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import djtools.dbfields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('systi', '0002_auto_20170223_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada_material',
            name='material',
            field=djtools.dbfields.ForeignKeyPlus(verbose_name=b'Material', blank=True, to='systi.Material', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='entrada_material',
            name='quantidade',
            field=djtools.dbfields.CharFieldPlus(max_length=30, null=True, verbose_name='Quantidade', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='entrada_material',
            name='usuario',
            field=djtools.dbfields.ForeignKeyPlus(blank=True, to=settings.AUTH_USER_MODEL, max_length=30, null=True, verbose_name='Usu\xe1rio'),
            preserve_default=True,
        ),
    ]

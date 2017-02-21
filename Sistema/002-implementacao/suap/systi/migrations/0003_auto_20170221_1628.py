# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import djtools.dbfields


class Migration(migrations.Migration):

    dependencies = [
        ('systi', '0002_auto_20170217_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='quantidade',
            field=djtools.dbfields.CharFieldPlus(max_length=30, null=True, verbose_name='Quantidade', blank=True),
            preserve_default=True,
        ),
    ]

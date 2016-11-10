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
            model_name='categoria',
            name='ativo',
            field=djtools.dbfields.OneToOneFieldPlus(null=True, blank=True, to='systi.Ativo'),
            preserve_default=True,
        ),
    ]

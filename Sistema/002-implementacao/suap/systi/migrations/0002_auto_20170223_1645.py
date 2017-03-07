# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('systi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada_material',
            name='nota_fornecimento',
            field=models.FileField(upload_to=b'systi/notasFornecimento/', null=True, verbose_name='Nota de Fornecimento', blank=True),
            preserve_default=True,
        ),
    ]

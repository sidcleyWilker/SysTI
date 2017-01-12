# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import djtools.dbfields


class Migration(migrations.Migration):

    dependencies = [
        ('systi', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='emprestimo',
            options={'verbose_name': 'Empr\xe9stimo', 'verbose_name_plural': 'Empr\xe9stimos'},
        ),
        migrations.AlterModelOptions(
            name='transferencia',
            options={'verbose_name': 'Transfer\xeancia', 'verbose_name_plural': 'Transfer\xeancias'},
        ),
        migrations.AlterField(
            model_name='servicoexterno',
            name='anexar_registro_servico',
            field=models.FileField(upload_to=b'', null=True, verbose_name=b'Anexar Registro do Servi\xc3\xa7o', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='servicoexterno',
            name='tipo_servico',
            field=djtools.dbfields.CharFieldPlus(default=b'Manuten\xc3\xa7\xc3\xa3o', max_length=25, verbose_name='Tipo do Servi\xe7o', choices=[(b'Manuten\xc3\xa7\xc3\xa3o', b'Manuten\xc3\xa7\xc3\xa3o'), (b'Suporte', b'Suporte')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='servicointerno',
            name='anexar_registro_servico',
            field=models.FileField(upload_to=b'', null=True, verbose_name=b'Anexar Registro do Servi\xc3\xa7o', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='servicointerno',
            name='tipo_servico',
            field=djtools.dbfields.CharFieldPlus(default=b'Manuten\xc3\xa7\xc3\xa3o', max_length=25, verbose_name='Tipo do Servi\xe7o', choices=[(b'Manuten\xc3\xa7\xc3\xa3o', b'Manuten\xc3\xa7\xc3\xa3o'), (b'Suporte', b'Suporte')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='transferencia',
            name='motivo_transferencia',
            field=djtools.dbfields.CharFieldPlus(default='Chamdo', max_length=30, verbose_name='Motivo da Transfer\xeancia', choices=[('E-mail', 'E-mail'), ('Chamdo', 'Chamdo'), ('Memorando', 'Memorando')]),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import djtools.dbfields


class Migration(migrations.Migration):

    dependencies = [
        ('systi', '0003_acessobiometrico_atributo_valoratt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acessobiometrico',
            name='aluno',
            field=djtools.dbfields.ForeignKeyPlus(verbose_name='Aluno', blank=True, to='edu.Aluno', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='acessobiometrico',
            name='data_registro',
            field=djtools.dbfields.DateFieldPlus(max_length=255, verbose_name='Data do Registro'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='acessobiometrico',
            name='servidor',
            field=djtools.dbfields.ForeignKeyPlus(verbose_name='Servidor do IF', blank=True, to='rh.Servidor', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='acessobiometrico',
            name='tipo_do_usuario',
            field=djtools.dbfields.CharFieldPlus(default=b'Aluno', max_length=10, verbose_name='Tipo do Usu\xe1rio', choices=[(b'Servidor', b'Servidor'), (b'Aluno', b'Aluno')]),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ChalitaCrinigan', '0024_auto_20160107_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propiedad',
            name='estado',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='propiedad',
            name='nombre',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='propiedad',
            name='superficieCubierta',
            field=models.CharField(max_length=200),
        ),
    ]

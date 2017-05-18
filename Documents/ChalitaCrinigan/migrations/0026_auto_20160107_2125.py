# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ChalitaCrinigan', '0025_auto_20160107_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propiedad',
            name='estado',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='propiedad',
            name='habitaciones',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='propiedad',
            name='nombre',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='propiedad',
            name='superficieCubierta',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='propiedad',
            name='superficieTotal',
            field=models.CharField(max_length=20),
        ),
    ]

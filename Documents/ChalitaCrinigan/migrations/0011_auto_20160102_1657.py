# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ChalitaCrinigan', '0010_auto_20160102_1619'),
    ]

    operations = [
        migrations.AddField(
            model_name='propiedad',
            name='textoListado',
            field=models.TextField(default=2),
            preserve_default=False,
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

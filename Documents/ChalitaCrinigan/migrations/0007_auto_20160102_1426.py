# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ChalitaCrinigan', '0006_auto_20151220_1738'),
    ]

    operations = [
        migrations.AddField(
            model_name='propiedad',
            name='superficieCubierta',
            field=models.IntegerField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='propiedad',
            name='cocheras',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='propiedad',
            name='precio',
            field=models.IntegerField(max_length=20),
        ),
        migrations.AlterField(
            model_name='propiedad',
            name='superficieTotal',
            field=models.IntegerField(max_length=20),
        ),
    ]

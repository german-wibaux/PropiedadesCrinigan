# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ChalitaCrinigan', '0018_auto_20160104_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propiedad',
            name='banios',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='propiedad',
            name='textoListado',
            field=models.TextField(default=b'vacio', max_length=112),
        ),
    ]

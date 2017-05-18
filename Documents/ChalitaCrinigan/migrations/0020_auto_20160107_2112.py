# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ChalitaCrinigan', '0019_auto_20160107_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propiedad',
            name='textoListado',
            field=models.CharField(default=b'vacio', max_length=112),
        ),
    ]

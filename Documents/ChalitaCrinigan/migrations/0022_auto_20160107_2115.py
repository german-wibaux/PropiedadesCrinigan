# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ChalitaCrinigan', '0021_auto_20160107_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propiedad',
            name='textoListado',
            field=models.TextField(default=b'vacio'),
        ),
    ]

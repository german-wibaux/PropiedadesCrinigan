# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ChalitaCrinigan', '0012_auto_20160102_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propiedad',
            name='geolocalizacion',
            field=models.TextField(null=True, blank=True),
        ),
    ]

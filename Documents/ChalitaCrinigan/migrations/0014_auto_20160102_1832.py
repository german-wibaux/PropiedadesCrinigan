# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ChalitaCrinigan', '0013_auto_20160102_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propiedad',
            name='banios',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='propiedad',
            name='habitaciones',
            field=models.CharField(max_length=20),
        ),
    ]

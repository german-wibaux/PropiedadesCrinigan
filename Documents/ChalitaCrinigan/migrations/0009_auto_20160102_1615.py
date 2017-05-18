# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ChalitaCrinigan', '0008_auto_20160102_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propiedad',
            name='precio',
            field=models.CharField(max_length=40),
        ),
    ]

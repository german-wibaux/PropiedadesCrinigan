# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ChalitaCrinigan', '0007_auto_20160102_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propiedad',
            name='codigo',
            field=models.CharField(max_length=40),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ChalitaCrinigan', '0009_auto_20160102_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propiedad',
            name='precio',
            field=models.TextField(),
        ),
    ]

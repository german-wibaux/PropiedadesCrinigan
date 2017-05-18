# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ChalitaCrinigan', '0022_auto_20160107_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propiedad',
            name='habitaciones',
            field=models.CharField(max_length=200),
        ),
    ]

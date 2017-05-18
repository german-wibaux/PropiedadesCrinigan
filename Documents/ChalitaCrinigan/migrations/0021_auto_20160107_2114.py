# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ChalitaCrinigan', '0020_auto_20160107_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propiedad',
            name='banios',
            field=models.CharField(max_length=100),
        ),
    ]

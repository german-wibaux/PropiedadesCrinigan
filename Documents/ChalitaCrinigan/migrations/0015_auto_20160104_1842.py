# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import thumbs


class Migration(migrations.Migration):

    dependencies = [
        ('ChalitaCrinigan', '0014_auto_20160102_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propiedad',
            name='banios',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='propiedad',
            name='imagen1',
            field=thumbs.ImageWithThumbsField(default=b'../chalita/defecto/images.jpeg', null=True, upload_to=b'chalita', blank=True),
        ),
    ]

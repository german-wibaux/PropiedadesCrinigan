# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import thumbs


class Migration(migrations.Migration):

    dependencies = [
        ('ChalitaCrinigan', '0004_auto_20151219_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propiedad',
            name='imagen1',
            field=thumbs.ImageWithThumbsField(null=True, upload_to=b'chalita'),
        ),
    ]

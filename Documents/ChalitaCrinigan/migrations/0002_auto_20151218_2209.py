# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import thumbs


class Migration(migrations.Migration):

    dependencies = [
        ('ChalitaCrinigan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propiedad',
            name='imagen1',
            field=thumbs.ImageWithThumbsField(default=b'../static/images/5.jpg', upload_to=b'chalita'),
        ),
    ]

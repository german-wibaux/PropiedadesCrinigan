# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import thumbs


class Migration(migrations.Migration):

    dependencies = [
        ('ChalitaCrinigan', '0016_auto_20160104_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propiedad',
            name='imagen1',
            field=thumbs.ImageWithThumbsField(default=b'chalita/defecto/images.jpeg', null=True, upload_to=b'chalita', blank=True),
        ),
    ]

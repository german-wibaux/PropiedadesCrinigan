# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import thumbs


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Localidad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Propiedad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=20)),
                ('descripcion', models.TextField()),
                ('codigo', models.IntegerField(max_length=20)),
                ('precio', models.IntegerField(max_length=15)),
                ('superficieTotal', models.IntegerField(max_length=10)),
                ('habitaciones', models.IntegerField(max_length=2)),
                ('banios', models.IntegerField(max_length=2)),
                ('cocheras', models.IntegerField(max_length=2)),
                ('geolocalizacion', models.TextField()),
                ('disponible', models.BooleanField()),
                ('estado', models.CharField(max_length=20)),
                ('imagen1', thumbs.ImageWithThumbsField(upload_to=b'chalita')),
                ('imagen2', thumbs.ImageWithThumbsField(upload_to=b'chalita')),
                ('imagen3', thumbs.ImageWithThumbsField(upload_to=b'chalita')),
                ('imagen4', thumbs.ImageWithThumbsField(upload_to=b'chalita')),
                ('imagen5', thumbs.ImageWithThumbsField(upload_to=b'chalita')),
                ('imagen6', thumbs.ImageWithThumbsField(upload_to=b'chalita')),
                ('imagen7', thumbs.ImageWithThumbsField(upload_to=b'chalita')),
                ('imagen8', thumbs.ImageWithThumbsField(upload_to=b'chalita')),
                ('imagen9', thumbs.ImageWithThumbsField(upload_to=b'chalita')),
                ('imagen10', thumbs.ImageWithThumbsField(upload_to=b'chalita')),
                ('imagen11', thumbs.ImageWithThumbsField(upload_to=b'chalita')),
                ('imagen12', thumbs.ImageWithThumbsField(upload_to=b'chalita')),
                ('imagen13', thumbs.ImageWithThumbsField(upload_to=b'chalita')),
                ('imagen14', thumbs.ImageWithThumbsField(upload_to=b'chalita')),
                ('imagen15', thumbs.ImageWithThumbsField(upload_to=b'chalita')),
                ('imagen16', thumbs.ImageWithThumbsField(upload_to=b'chalita')),
                ('imagen17', thumbs.ImageWithThumbsField(upload_to=b'chalita')),
                ('imagen18', thumbs.ImageWithThumbsField(upload_to=b'chalita')),
                ('imagen19', thumbs.ImageWithThumbsField(upload_to=b'chalita')),
                ('imagen20', thumbs.ImageWithThumbsField(upload_to=b'chalita')),
                ('imagen21', thumbs.ImageWithThumbsField(upload_to=b'chalita')),
                ('imagen22', thumbs.ImageWithThumbsField(upload_to=b'chalita')),
                ('imagen23', thumbs.ImageWithThumbsField(upload_to=b'chalita')),
                ('imagen24', thumbs.ImageWithThumbsField(upload_to=b'chalita')),
                ('imagen25', thumbs.ImageWithThumbsField(upload_to=b'chalita')),
                ('localidad', models.ForeignKey(to='ChalitaCrinigan.Localidad')),
            ],
        ),
        migrations.CreateModel(
            name='TipoOperacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TipoPropiedad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='propiedad',
            name='tipoOperacion',
            field=models.ForeignKey(to='ChalitaCrinigan.TipoOperacion'),
        ),
        migrations.AddField(
            model_name='propiedad',
            name='tipoPropiedad',
            field=models.ForeignKey(to='ChalitaCrinigan.TipoPropiedad'),
        ),
    ]

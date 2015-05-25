# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('atelier', '0004_auto_20150524_2309'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlbumArtworkAttr',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_decided', models.DateField()),
            ],
        ),
        migrations.RemoveField(
            model_name='album',
            name='artwork_attr',
        ),
        migrations.AlterField(
            model_name='album',
            name='release_date',
            field=models.DateTimeField(verbose_name=b'release date'),
        ),
        migrations.AddField(
            model_name='albumartworkattr',
            name='album',
            field=models.ForeignKey(to='atelier.Album'),
        ),
        migrations.AddField(
            model_name='albumartworkattr',
            name='artwork_attr',
            field=models.ForeignKey(to='atelier.ArtworkAttr'),
        ),
        migrations.AddField(
            model_name='album',
            name='members',
            field=models.ManyToManyField(to='atelier.ArtworkAttr', through='atelier.AlbumArtworkAttr'),
        ),
    ]

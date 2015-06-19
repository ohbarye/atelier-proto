# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'album name')),
                ('seven_static_id', models.IntegerField(unique=True, null=True, verbose_name=b'7static id', blank=True)),
                ('release_date', models.DateTimeField(null=True, verbose_name=b'release date', blank=True)),
                ('artwork_url', models.CharField(max_length=255, verbose_name=b'artwork url', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='AlbumArtworkClass',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score_rank', models.IntegerField(verbose_name=b'rank')),
                ('score', models.DecimalField(verbose_name=b'score', max_digits=18, decimal_places=17)),
                ('album', models.ForeignKey(to='atelier.Album')),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'artist name')),
            ],
        ),
        migrations.CreateModel(
            name='ArtworkClass',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('class_id', models.CharField(unique=True, max_length=9, verbose_name=b'class id')),
                ('class_id_number', models.IntegerField(unique=True, verbose_name=b'class id number')),
                ('name', models.CharField(max_length=255, verbose_name=b'type name')),
                ('name_jp', models.CharField(max_length=255, verbose_name=b'type name in Japanese')),
            ],
        ),
        migrations.AddField(
            model_name='albumartworkclass',
            name='artwork_class',
            field=models.ForeignKey(to='atelier.ArtworkClass'),
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(related_name='impressions', verbose_name=b'artist', to='atelier.Artist'),
        ),
        migrations.AddField(
            model_name='album',
            name='artwork_class',
            field=models.ManyToManyField(to='atelier.ArtworkClass', through='atelier.AlbumArtworkClass'),
        ),
        migrations.AlterUniqueTogether(
            name='albumartworkclass',
            unique_together=set([('album', 'artwork_class', 'score_rank')]),
        ),
    ]

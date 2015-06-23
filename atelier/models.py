# -*- coding: utf-8 -*-
import json
from django.db import models
from collections import OrderedDict

class Artist(models.Model):
    name = models.CharField('artist name', max_length=255)

    def __unicode__(self):
        return self.name

    def serialize(self):
        return OrderedDict([
            ('name', self.name)
        ])

class ArtworkClass(models.Model):
    class_id        = models.CharField('class id', max_length=9, unique=True)
    class_id_number = models.IntegerField('class id number', unique=True)
    name            = models.CharField('type name', max_length=255)
    name_jp         = models.CharField('type name in Japanese', max_length=255)

    def __unicode__(self):
        return self.name

    def serialize(self):
        return OrderedDict([
            ('class_id', self.class_id),
            ('class_id_number', self.class_id_number),
            ('name', self.name),
            ('name_jp', self.name_jp)
        ])

class Album(models.Model):
    name            = models.CharField('album name', max_length=255)
    seven_static_id = models.IntegerField('7static id', blank=True, null=True, unique=True)
    artist          = models.ForeignKey(Artist, verbose_name='artist', related_name='impressions')
    release_date    = models.DateTimeField('release date', blank=True, null=True)
    artwork_class   = models.ManyToManyField(ArtworkClass, through='AlbumArtworkClass')
    artwork_url     = models.CharField('artwork url', max_length=255, blank=True)

    def __unicode__(self):
        return self.name

    def serialize(self):
        return OrderedDict([
            ('name', self.name),
            ('seven_static_id', self.seven_static_id),
            ('artwork_url', self.artwork_url),
            ('artist', self.artist.serialize())
        ])

class AlbumArtworkClass(models.Model):
    album         = models.ForeignKey(Album)
    artwork_class = models.ForeignKey(ArtworkClass)
    score_rank    = models.IntegerField('rank')
    score         = models.DecimalField('score', max_digits=18, decimal_places=17)

    def serialize(self):
        return OrderedDict([
            ('album', self.album.serialize()),
            ('score_rank', self.score_rank),
            ('score', float(self.score))
        ])

    class Meta:
        unique_together=(('album','artwork_class','score_rank'))

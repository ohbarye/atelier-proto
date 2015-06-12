# -*- coding: utf-8 -*-
from django.db import models

class Artist(models.Model):
    name = models.CharField('artist name', max_length=255)

    def __unicode__(self):
        return self.name

class ArtworkClass(models.Model):
    class_id = models.CharField('class id', max_length=9, unique=True)
    class_id_number = models.IntegerField('class id number', unique=True)
    name = models.CharField('type name', max_length=255)

    def __unicode__(self):
        return self.name

class Album(models.Model):
    name = models.CharField('album name', max_length=255)
    seven_static_id = models.IntegerField('7static id', blank=True, null=True, unique=True)
    artist = models.ForeignKey(Artist, verbose_name='artist', related_name='impressions')
    release_date = models.DateTimeField('release date', blank=True, null=True)
    artwork_class = models.ManyToManyField(ArtworkClass, through='AlbumArtworkClass')
    artwork_url = models.CharField('artwork url', max_length=255, blank=True)

    def __unicode__(self):
        return self.name

class AlbumArtworkClass(models.Model):
    album = models.ForeignKey(Album)
    artwork_class = models.ForeignKey(ArtworkClass)
    score_rank = models.IntegerField('rank')
    score = models.DecimalField('score', max_digits=18, decimal_places=17)

    class Meta:
        unique_together=(('album','artwork_class','score_rank'))

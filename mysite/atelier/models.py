# -*- coding: utf-8 -*-
from django.db import models
from django_enumfield import enum

class Artist(models.Model):
    '''アーティスト'''
    name = models.CharField('artist name', max_length=255)

    def __unicode__(self):
        return self.name

class ImageType(enum.Enum):
    '''アルバムの属性(犬とか猫とか)'''
    DOG = 1
    CAT = 2
    LADY = 3

    labels = {
        CAT: 'Cat',
        DOG: 'Dog',
        LADY: 'Lady',
    }

class ArtworkAttr(models.Model):
    '''アルバムの属性(犬とか猫とか)'''
    name = models.CharField('type name', max_length=255)
    image_type = enum.EnumField(ImageType)

    def __unicode__(self):
        return self.name

class Album(models.Model):
    '''アルバム'''
    name = models.CharField('album name', max_length=255)
    artist = models.ForeignKey(Artist, verbose_name='artist', related_name='impressions')
    release_date = models.DateTimeField('release date', blank=True, null=True)
    members = models.ManyToManyField(ArtworkAttr, through='AlbumArtworkAttr')
    artwork_url = models.CharField('artwork url', max_length=255, blank=True)

    def __unicode__(self):
        return self.name

class AlbumArtworkAttr(models.Model):
    album = models.ForeignKey(Album)
    artwork_attr = models.ForeignKey(ArtworkAttr)
    date_decided = models.DateField()

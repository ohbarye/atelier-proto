# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('atelier', '0006_artworkattr_image_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='artwork_url',
            field=models.CharField(max_length=255, verbose_name=b'artwork url', blank=True),
        ),
    ]

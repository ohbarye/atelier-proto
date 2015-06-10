# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('atelier', '0011_artworkattr_add_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='seven_static_id',
            field=models.IntegerField(null=True, verbose_name=b'7static id', blank=True),
        ),
    ]

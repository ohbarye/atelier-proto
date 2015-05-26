# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('atelier', '0008_auto_20150525_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='release_date',
            field=models.DateTimeField(null=True, verbose_name=b'release date', blank=True),
        ),
    ]

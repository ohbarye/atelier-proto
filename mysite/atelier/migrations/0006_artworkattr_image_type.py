# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('atelier', '0005_auto_20150524_2316'),
    ]

    operations = [
        migrations.AddField(
            model_name='artworkattr',
            name='image_type',
            field=models.IntegerField(default=1),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('atelier', '0010_auto_20150525_2359'),
    ]

    operations = [
        migrations.AddField(
            model_name='artworkattr',
            name='add_date',
            field=models.DateTimeField(null=True, verbose_name=b'add date', blank=True),
        ),
    ]

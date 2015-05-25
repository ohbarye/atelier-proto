# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('atelier', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='categories',
            field=models.ManyToManyField(to='atelier.Category'),
        ),
    ]

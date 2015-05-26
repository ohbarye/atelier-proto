# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('atelier', '0009_auto_20150525_0006'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='members',
            new_name='artwork_attr',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('atelier', '0002_album_categories'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='ArtworkAttribute',
        ),
        migrations.RenameField(
            model_name='album',
            old_name='categories',
            new_name='artwork_attribute',
        ),
    ]

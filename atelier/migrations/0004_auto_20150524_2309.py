# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('atelier', '0003_auto_20150524_2308'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ArtworkAttribute',
            new_name='ArtworkAttr',
        ),
        migrations.RenameField(
            model_name='album',
            old_name='artwork_attribute',
            new_name='artwork_attr',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0008_auto_20150327_1134'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dataset',
            old_name='short_name',
            new_name='slug',
        ),
        migrations.RenameField(
            model_name='experiment',
            old_name='short_name',
            new_name='slug',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='short_name',
            new_name='slug',
        ),
    ]

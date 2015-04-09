# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0012_auto_20150409_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiment',
            name='meta',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20150331_1248'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='activated',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='complete',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]

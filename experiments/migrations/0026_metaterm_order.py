# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0025_auto_20150707_1831'),
    ]

    operations = [
        migrations.AddField(
            model_name='metaterm',
            name='order',
            field=models.IntegerField(default=0),
        ),
    ]

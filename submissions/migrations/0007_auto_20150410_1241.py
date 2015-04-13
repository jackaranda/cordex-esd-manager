# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0006_auto_20150409_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='modified',
            field=models.DateTimeField(auto_now=True),
            preserve_default=True,
        ),
    ]

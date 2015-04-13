# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0016_auto_20150409_1424'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeperiod',
            name='exclude',
            field=models.ManyToManyField(to='experiments.TimePeriod'),
            preserve_default=True,
        ),
    ]

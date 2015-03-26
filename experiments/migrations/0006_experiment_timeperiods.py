# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0005_auto_20150326_1347'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiment',
            name='timeperiods',
            field=models.ManyToManyField(to='experiments.TimePeriod', through='experiments.ExperimentTimePeriods'),
            preserve_default=True,
        ),
    ]

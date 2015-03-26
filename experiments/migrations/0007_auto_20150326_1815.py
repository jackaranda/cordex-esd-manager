# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0006_experiment_timeperiods'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiment',
            name='parent',
            field=models.ForeignKey(related_name='children', to='experiments.Experiment', null=True),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0015_remove_experiment_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experiment',
            name='parent',
        ),
        migrations.AddField(
            model_name='experiment',
            name='meta',
            field=models.ForeignKey(related_name='experiments', blank=True, to='experiments.MetaExperiment', null=True),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0004_experiment_parent'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExperimentTimePeriods',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(default=b'', max_length=20, blank=True, choices=[(b'calibration', b'Calibration period'), (b'validation', b'Validation period')])),
                ('experiment', models.ForeignKey(to='experiments.Experiment')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TimePeriod',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('short_name', models.CharField(default=b'', max_length=50, blank=True)),
                ('begin', models.DateTimeField(default=datetime.datetime(1900, 1, 1, 0, 0))),
                ('end', models.DateTimeField(default=datetime.datetime(1999, 12, 31, 0, 0))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='experimenttimeperiods',
            name='timeperiod',
            field=models.ForeignKey(to='experiments.TimePeriod'),
            preserve_default=True,
        ),
    ]

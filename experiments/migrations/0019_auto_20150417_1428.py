# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0018_remove_timeperiod_exclude'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExperimentVariables',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(default=b'', max_length=20, blank=True, choices=[(b'forcing', b'Forcing'), (b'output', b'Output')])),
                ('experiment', models.ForeignKey(to='experiments.Experiment')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Variable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('short_name', models.SlugField(default=b'', unique=True)),
                ('long_name', models.CharField(default=b'', max_length=100, blank=True)),
                ('standard_name', models.CharField(default=b'', max_length=100, blank=True)),
                ('units', models.CharField(max_length=15)),
                ('comments', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='experimentvariables',
            name='variable',
            field=models.ForeignKey(to='experiments.Variable'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='experiment',
            name='variables',
            field=models.ManyToManyField(to='experiments.Variable', through='experiments.ExperimentVariables'),
            preserve_default=True,
        ),
    ]

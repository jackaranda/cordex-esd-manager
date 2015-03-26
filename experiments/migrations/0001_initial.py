# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(default=b'', max_length=20, blank=True, choices=[(b'observed', b'Observed datasets'), (b're-analysis', b'Re-analysis datasets'), (b'CMIP5', b'CMIP5 Models')])),
                ('short_name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('source_url', models.URLField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Experiment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('short_name', models.CharField(default=b'', max_length=50)),
                ('description', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(to='profiles.Profile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ExperimentDatasets',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(default=b'', max_length=20, blank=True, choices=[(b'predictor', b'Predictor'), (b'predictand', b'Predictand')])),
                ('dataset', models.ForeignKey(to='experiments.Dataset')),
                ('experiment', models.ForeignKey(to='experiments.Experiment')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='experiment',
            name='datasets',
            field=models.ManyToManyField(to='experiments.Dataset', through='experiments.ExperimentDatasets'),
            preserve_default=True,
        ),
    ]

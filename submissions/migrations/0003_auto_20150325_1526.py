# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0002_auto_20150325_1423'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExperimentDatasets',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(default=b'', max_length=20, blank=True, choices=[(b'predictor', b'Predictor'), (b'predictand', b'Predictand')])),
                ('dataset', models.ForeignKey(to='submissions.Dataset')),
                ('experiment', models.ForeignKey(to='submissions.Experiment')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='experiment',
            name='datasets',
            field=models.ManyToManyField(to='submissions.Dataset', through='submissions.ExperimentDatasets'),
            preserve_default=True,
        ),
    ]

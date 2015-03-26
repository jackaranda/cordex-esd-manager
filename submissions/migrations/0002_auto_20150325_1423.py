# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20150116_1453'),
        ('submissions', '0001_initial'),
    ]

    operations = [
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
            name='Model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=50)),
                ('description', models.TextField(default=b'', blank=True)),
                ('contact', models.ForeignKey(to='profiles.Profile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='esdexperiment',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='esdmodel',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='submission',
            name='esd_experiment',
        ),
        migrations.DeleteModel(
            name='ESDExperiment',
        ),
        migrations.AddField(
            model_name='submission',
            name='experiment',
            field=models.ForeignKey(to='submissions.Experiment', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='submission',
            name='model',
            field=models.ForeignKey(to='submissions.Model'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='ESDModel',
        ),
    ]

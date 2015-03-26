# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20150116_1453'),
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
            name='ESDExperiment',
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
            name='ESDModel',
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
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('version', models.IntegerField(default=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField()),
                ('notes', models.TextField(default=b'', blank=True)),
                ('archive_path', models.CharField(default=b'', max_length=500, blank=True)),
                ('archive_filename', models.CharField(default=b'', max_length=500, blank=True)),
                ('esd_experiment', models.ForeignKey(to='submissions.ESDExperiment')),
                ('model', models.ForeignKey(to='submissions.ESDModel')),
                ('owner', models.ForeignKey(to='profiles.Profile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(null=True)),
                ('format', models.CharField(default=b'txt', max_length=10, choices=[(b'txt', b'Claris Text Format'), (b'ziptxt', b'Zipped text format'), (b'nc', b'netcdf')])),
                ('mode', models.CharField(default=b'POST', max_length=10, choices=[(b'POST', b'HTTP POST'), (b'PUT', b'FTP PUT')])),
                ('path', models.CharField(default=b'', max_length=500, blank=True)),
                ('filename', models.CharField(default=b'', max_length=500, blank=True)),
                ('submission', models.ForeignKey(to='submissions.Submission')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Variable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('short_name', models.CharField(max_length=20)),
                ('standard_name', models.CharField(max_length=50)),
                ('long_name', models.CharField(max_length=50)),
                ('units', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

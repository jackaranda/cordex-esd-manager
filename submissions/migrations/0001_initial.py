# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0001_initial'),
        ('profiles', '0001_initial'),
    ]

    operations = [
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
                ('experiment', models.ForeignKey(to='experiments.Experiment', null=True)),
                ('model', models.ForeignKey(to='submissions.Model')),
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

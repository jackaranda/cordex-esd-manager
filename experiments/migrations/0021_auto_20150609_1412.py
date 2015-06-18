# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0020_auto_20150424_1126'),
    ]

    operations = [
        migrations.CreateModel(
            name='MetaCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField()),
                ('description', models.TextField(default=b'')),
            ],
        ),
        migrations.CreateModel(
            name='MetaDependencies',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.TextField(choices=[(b'Equal', b'equal')])),
            ],
        ),
        migrations.CreateModel(
            name='MetaTerm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.SlugField()),
                ('long_name', models.CharField(default=b'', max_length=100)),
                ('help_text', models.TextField(default=b'', blank=True)),
                ('multiple', models.BooleanField(default=False)),
                ('category', models.ForeignKey(to='experiments.MetaCategory')),
            ],
        ),
        migrations.CreateModel(
            name='MetaValues',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(max_length=100)),
                ('term', models.ForeignKey(related_name='values', to='experiments.MetaTerm')),
            ],
        ),
        migrations.AddField(
            model_name='metadependencies',
            name='depends_on',
            field=models.ForeignKey(related_name='depended_on', to='experiments.MetaTerm'),
        ),
        migrations.AddField(
            model_name='metadependencies',
            name='depends_value',
            field=models.ForeignKey(to='experiments.MetaValues'),
        ),
        migrations.AddField(
            model_name='metaexperiment',
            name='metadata_category',
            field=models.ForeignKey(blank=True, to='experiments.MetaCategory', null=True),
        ),
    ]

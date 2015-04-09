# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20150331_1248'),
        ('experiments', '0011_auto_20150331_1425'),
    ]

    operations = [
        migrations.CreateModel(
            name='MetaExperiment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField()),
                ('title', models.CharField(default=b'', max_length=50)),
                ('description', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(to='profiles.Profile')),
                ('project', models.ForeignKey(to='experiments.Project', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='meta',
            field=models.BooleanField(),
            preserve_default=True,
        ),
    ]

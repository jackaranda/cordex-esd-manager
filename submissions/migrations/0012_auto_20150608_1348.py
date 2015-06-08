# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0011_auto_20150608_1345'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelMetaCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField()),
                ('description', models.TextField(default=b'')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ModelMetaDependencies',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.TextField(choices=[(b'Equal', b'equal')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ModelMetaTerm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.SlugField()),
                ('long_name', models.CharField(default=b'', max_length=100)),
                ('help_text', models.TextField(default=b'', blank=True)),
                ('multiple', models.BooleanField(default=False)),
                ('category', models.ForeignKey(to='submissions.ModelMetaCategory')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ModelMetaValues',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(max_length=100)),
                ('term', models.ForeignKey(related_name='values', to='submissions.ModelMetaTerm')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='modelmetadependencies',
            name='depends_on',
            field=models.ForeignKey(related_name='depended_on', to='submissions.ModelMetaTerm'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='modelmetadependencies',
            name='depends_value',
            field=models.ForeignKey(to='submissions.ModelMetaValues'),
            preserve_default=True,
        ),
    ]

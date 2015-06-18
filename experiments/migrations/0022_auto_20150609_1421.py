# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0015_auto_20150609_1421'),
        ('experiments', '0021_auto_20150609_1412'),
    ]

    operations = [
        migrations.CreateModel(
            name='MetaDependency',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.TextField(choices=[(b'Equal', b'equal')])),
                ('depends_on', models.ForeignKey(related_name='depended_on', to='experiments.MetaTerm')),
            ],
        ),
        migrations.CreateModel(
            name='MetaValue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(max_length=100)),
                ('term', models.ForeignKey(related_name='values', to='experiments.MetaTerm')),
            ],
        ),
        migrations.RemoveField(
            model_name='metadependencies',
            name='depends_on',
        ),
        migrations.RemoveField(
            model_name='metadependencies',
            name='depends_value',
        ),
        migrations.RemoveField(
            model_name='metavalues',
            name='term',
        ),
        migrations.DeleteModel(
            name='MetaDependencies',
        ),
        migrations.DeleteModel(
            name='MetaValues',
        ),
        migrations.AddField(
            model_name='metadependency',
            name='depends_value',
            field=models.ForeignKey(to='experiments.MetaValue'),
        ),
    ]

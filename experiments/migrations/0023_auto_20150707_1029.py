# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0022_auto_20150609_1421'),
    ]

    operations = [
        migrations.CreateModel(
            name='MetaControlledValue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='metadependency',
            name='depends_on',
        ),
        migrations.RemoveField(
            model_name='metadependency',
            name='depends_value',
        ),
        migrations.RemoveField(
            model_name='metavalue',
            name='term',
        ),
        migrations.AddField(
            model_name='metaterm',
            name='freetext',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='MetaDependency',
        ),
    ]

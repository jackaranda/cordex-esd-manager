# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0021_auto_20150609_1412'),
        ('submissions', '0013_auto_20150609_1405'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelMeta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('term', models.ForeignKey(to='experiments.MetaTerm')),
                ('value', models.ForeignKey(to='experiments.MetaValues')),
            ],
        ),
        migrations.AddField(
            model_name='model',
            name='meta_data',
            field=models.ManyToManyField(to='submissions.ModelMeta'),
        ),
    ]

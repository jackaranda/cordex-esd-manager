# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0024_auto_20150707_1029'),
    ]

    operations = [
        migrations.AddField(
            model_name='metaterm',
            name='target',
            field=models.CharField(default=b'', max_length=20, blank=True, choices=[(b'model', b'Model'), (b'submission', b'Submission')]),
        ),
        migrations.AlterField(
            model_name='metacontrolledvalue',
            name='term',
            field=models.ForeignKey(related_name='values', to='experiments.MetaTerm'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0023_auto_20150707_1029'),
        ('submissions', '0020_auto_20150707_1029'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MetaValue',
        ),
        migrations.AddField(
            model_name='metacontrolledvalue',
            name='term',
            field=models.ForeignKey(related_name='controlled_values', to='experiments.MetaTerm'),
        ),
    ]

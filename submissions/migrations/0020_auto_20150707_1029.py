# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0023_auto_20150707_1029'),
        ('submissions', '0019_auto_20150609_2004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='model',
            name='metadata',
        ),
        migrations.RemoveField(
            model_name='modelmeta',
            name='entry',
        ),
        migrations.AddField(
            model_name='modelmeta',
            name='term',
            field=models.ForeignKey(default=1, to='experiments.MetaTerm'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='modelmeta',
            name='value',
            field=models.CharField(default=b'', max_length=500),
        ),
    ]

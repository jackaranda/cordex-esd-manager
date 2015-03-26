# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0003_auto_20150326_1330'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiment',
            name='parent',
            field=models.ForeignKey(to='experiments.Experiment', null=True),
            preserve_default=True,
        ),
    ]

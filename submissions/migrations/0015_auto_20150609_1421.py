# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0014_auto_20150609_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelmeta',
            name='value',
            field=models.ForeignKey(to='experiments.MetaValue'),
        ),
    ]

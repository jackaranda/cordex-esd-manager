# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0012_auto_20150608_1348'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modelmetadependencies',
            name='depends_on',
        ),
        migrations.RemoveField(
            model_name='modelmetadependencies',
            name='depends_value',
        ),
        migrations.RemoveField(
            model_name='modelmetaterm',
            name='category',
        ),
        migrations.RemoveField(
            model_name='modelmetavalues',
            name='term',
        ),
        migrations.DeleteModel(
            name='ModelMetaCategory',
        ),
        migrations.DeleteModel(
            name='ModelMetaDependencies',
        ),
        migrations.DeleteModel(
            name='ModelMetaTerm',
        ),
        migrations.DeleteModel(
            name='ModelMetaValues',
        ),
    ]

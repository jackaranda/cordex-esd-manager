# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0007_auto_20150326_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='short_name',
            field=models.SlugField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='experiment',
            name='short_name',
            field=models.SlugField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='short_name',
            field=models.SlugField(),
            preserve_default=True,
        ),
    ]

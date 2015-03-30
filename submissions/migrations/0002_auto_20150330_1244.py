# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model',
            name='name',
            field=models.SlugField(default=b''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='variable',
            name='short_name',
            field=models.SlugField(max_length=20),
            preserve_default=True,
        ),
    ]

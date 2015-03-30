# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0002_auto_20150330_1244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='model',
            name='name',
        ),
        migrations.AddField(
            model_name='model',
            name='slug',
            field=models.SlugField(default='unknown'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='model',
            name='title',
            field=models.CharField(default=b'', max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='variable',
            name='short_name',
            field=models.CharField(max_length=20),
            preserve_default=True,
        ),
    ]

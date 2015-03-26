# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='country',
            field=models.CharField(max_length=3, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='institution',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
    ]

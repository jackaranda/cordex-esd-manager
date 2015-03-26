# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('experiments', '0002_auto_20150326_1326'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 26, 13, 30, 45, 283776, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='created_by',
            field=models.ForeignKey(to='profiles.Profile', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 26, 13, 30, 49, 357706, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='url',
            field=models.URLField(default=b''),
            preserve_default=True,
        ),
    ]

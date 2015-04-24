# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0019_auto_20150417_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variable',
            name='comments',
            field=models.TextField(default=b'', blank=True),
            preserve_default=True,
        ),
    ]

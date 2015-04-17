# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0007_auto_20150410_1241'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='status',
            field=models.CharField(default=b'unknown', max_length=200, blank=True),
            preserve_default=True,
        ),
    ]

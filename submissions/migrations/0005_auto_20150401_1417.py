# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0004_auto_20150330_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='uploaded',
            field=models.FileField(null=True, upload_to=b''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='upload',
            name='timestamp',
            field=models.DateTimeField(default=None, auto_now_add=True),
            preserve_default=True,
        ),
    ]

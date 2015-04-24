# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0009_delete_variable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
    ]

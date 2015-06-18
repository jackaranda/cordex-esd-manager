# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0016_auto_20150609_1839'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modelmeta',
            name='term',
        ),
    ]

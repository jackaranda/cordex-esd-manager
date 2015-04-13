# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0017_timeperiod_exclude'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timeperiod',
            name='exclude',
        ),
    ]

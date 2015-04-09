# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0014_remove_experiment_meta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experiment',
            name='project',
        ),
    ]

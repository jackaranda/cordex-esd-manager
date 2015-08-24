# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0026_metaterm_order'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MetaValues',
        ),
    ]

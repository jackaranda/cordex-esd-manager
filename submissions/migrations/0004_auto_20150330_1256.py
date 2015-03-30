# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0003_auto_20150330_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='submission',
            field=models.ForeignKey(related_name='uploads', to='submissions.Submission'),
            preserve_default=True,
        ),
    ]

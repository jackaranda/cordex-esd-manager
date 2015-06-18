# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0015_auto_20150609_1421'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='model',
            name='meta_data',
        ),
        migrations.AddField(
            model_name='modelmeta',
            name='model',
            field=models.ForeignKey(to='submissions.Model', null=True),
        ),
    ]

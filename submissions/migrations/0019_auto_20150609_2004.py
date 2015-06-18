# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0022_auto_20150609_1421'),
        ('submissions', '0018_auto_20150609_1943'),
    ]

    operations = [
        migrations.AddField(
            model_name='model',
            name='metadata',
            field=models.ManyToManyField(to='experiments.MetaValue'),
        ),
        migrations.AlterField(
            model_name='modelmeta',
            name='model',
            field=models.ForeignKey(related_name='metadata_old', to='submissions.Model', null=True),
        ),
    ]

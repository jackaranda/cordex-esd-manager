# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0017_remove_modelmeta_term'),
    ]

    operations = [
        migrations.RenameField(
            model_name='modelmeta',
            old_name='value',
            new_name='entry',
        ),
        migrations.AlterField(
            model_name='modelmeta',
            name='model',
            field=models.ForeignKey(related_name='metadata', to='submissions.Model', null=True),
        ),
    ]

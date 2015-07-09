# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0025_auto_20150707_1831'),
        ('submissions', '0020_auto_20150707_1029'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubmissionMeta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(default=b'', max_length=500)),
                ('submission', models.ForeignKey(related_name='metadata', to='submissions.Submission', null=True)),
                ('term', models.ForeignKey(to='experiments.MetaTerm')),
            ],
        ),
        migrations.AlterField(
            model_name='modelmeta',
            name='model',
            field=models.ForeignKey(related_name='metadata', to='submissions.Model', null=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage
import submissions.models


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0005_auto_20150401_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='uploaded',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(b'/home/cjack/work/projects/code/cordex-esd-manager/cordex_esd_manager/uploads/'), null=True, upload_to=submissions.models.make_upload_path),
            preserve_default=True,
        ),
    ]

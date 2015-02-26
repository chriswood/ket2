# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ketapp', '0011_uploadimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadimage',
            name='userid',
        ),
        migrations.DeleteModel(
            name='UploadImage',
        ),
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
            preserve_default=True,
        ),
    ]

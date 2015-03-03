# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ketapp', '0012_auto_20150226_0237'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo_height',
            field=models.CharField(max_length=10, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(height_field=b'photo_height', null=True, upload_to=b'', blank=True),
            preserve_default=True,
        ),
    ]

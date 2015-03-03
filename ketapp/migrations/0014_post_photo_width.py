# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ketapp', '0013_auto_20150301_0422'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo_width',
            field=models.CharField(max_length=10, null=True, blank=True),
            preserve_default=True,
        ),
    ]

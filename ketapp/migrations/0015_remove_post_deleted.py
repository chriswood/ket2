# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ketapp', '0014_post_photo_width'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='deleted',
        ),
    ]

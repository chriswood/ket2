# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ketapp', '0005_auto_20150209_0322'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='post',
            table='posts',
        ),
    ]

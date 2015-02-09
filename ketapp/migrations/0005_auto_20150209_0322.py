# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ketapp', '0004_auto_20150208_0513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='userid',
            field=models.ForeignKey(to='ketapp.User'),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('ketapp', '0006_auto_20150209_0324'),
        (b'auth', b'__first__'),
        (b'contenttypes', b'__first__'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='UserCustom',
        ),
        migrations.AlterField(
            model_name='post',
            name='userid',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterModelTable(
            name='usercustom',
            table='users_custom',
        ),
    ]

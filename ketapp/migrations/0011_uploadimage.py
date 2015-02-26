# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ketapp', '0010_auto_20150219_2225'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('message', models.TextField(max_length=500, verbose_name=b'message')),
                ('photo', models.ImageField(upload_to=b'/home/chris/code/images')),
                ('userid', models.ForeignKey(related_name='images', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'images',
            },
            bases=(models.Model,),
        ),
    ]

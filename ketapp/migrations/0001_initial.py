# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstname', models.CharField(max_length=40, verbose_name=b'first name')),
                ('lastname', models.CharField(max_length=40, verbose_name=b'last name')),
                ('email', models.EmailField(max_length=100, verbose_name=b'email', validators=[django.core.validators.EmailValidator()])),
                ('username', models.CharField(max_length=20, verbose_name=b'username', validators=[django.core.validators.MinValueValidator(3)])),
                ('password', models.CharField(max_length=50, verbose_name=b'password', validators=[django.core.validators.MinValueValidator(4)])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

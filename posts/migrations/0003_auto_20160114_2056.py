# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-14 20:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='draft',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='publish',
            field=models.DateField(default=datetime.datetime(2016, 1, 14, 20, 56, 8, 183934, tzinfo=utc)),
            preserve_default=False,
        ),
    ]

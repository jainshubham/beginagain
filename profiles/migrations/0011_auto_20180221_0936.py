# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-21 09:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0010_auto_20180218_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birth_date_time',
            field=models.DateTimeField(default=datetime.datetime(2000, 2, 8, 9, 36, 51, 159762)),
        ),
    ]

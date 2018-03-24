# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-18 15:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_auto_20180218_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birth_date_time',
            field=models.DateTimeField(default=datetime.datetime(2000, 2, 5, 15, 34, 57, 721842)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='eating_habit',
            field=models.IntegerField(choices=[(1, 'Non Vegetarian'), (0, 'Vegetarian')], default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='physical_status',
            field=models.IntegerField(choices=[(5, 'Critical'), (6, 'Maximal'), (1, 'Minor'), (2, 'Moderate'), (3, 'Serious'), (4, 'Severe')], default=3),
        ),
    ]
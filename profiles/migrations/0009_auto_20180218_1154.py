# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-18 11:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django_measurement.models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_auto_20180118_1444'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='username',
        ),
        migrations.AlterField(
            model_name='profile',
            name='about_me',
            field=models.CharField(blank=True, default='', max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.PositiveIntegerField(default=18, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='birth_date_time',
            field=models.DateTimeField(default=datetime.datetime(2000, 2, 5, 11, 52, 33, 31418)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='body_type',
            field=models.IntegerField(choices=[(1, 'Average'), (2, 'Overweight'), (0, 'Slim')], default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='caste',
            field=models.CharField(blank=True, default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(blank=True, default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='country',
            field=models.CharField(blank=True, default='Indian', max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='drinking_habit',
            field=models.IntegerField(choices=[(0, 'Non Drinker'), (2, 'Occasional'), (1, 'Regular')], default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='eating_habit',
            field=models.IntegerField(choices=[(2, 'Non Vegetarian'), (1, 'Vegetarian')], default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='education',
            field=models.CharField(blank=True, default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.IntegerField(choices=[(1, 'Female'), (0, 'Male'), (2, 'Other')], default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gothram',
            field=models.CharField(blank=True, default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='height',
            field=django_measurement.models.MeasurementField(default=100, measurement_class='Distance'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='marital_status',
            field=models.IntegerField(choices=[(1, 'Divorced'), (3, 'Married'), (0, 'Unmarried'), (2, 'Widowed')], default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='mother_tongue',
            field=models.CharField(blank=True, default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='physical_status',
            field=models.IntegerField(choices=[(5, 'Critical'), (6, 'Maximal'), (1, 'Minor'), (2, 'Moderate'), (3, 'Serious'), (4, 'Severe')], default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pincode',
            field=models.CharField(blank=True, default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='place_of_birth',
            field=models.CharField(blank=True, default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='religion',
            field=models.CharField(blank=True, default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='require_details',
            field=models.CharField(blank=True, default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='smoking_habit',
            field=models.IntegerField(choices=[(0, 'Non Smoker'), (2, 'Occasional'), (1, 'Regular')], default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='star',
            field=models.CharField(blank=True, default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='state',
            field=models.CharField(blank=True, default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='weight',
            field=django_measurement.models.MeasurementField(default=60, measurement_class='Mass'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='zodiac',
            field=models.CharField(blank=True, default='', max_length=30),
            preserve_default=False,
        ),
    ]

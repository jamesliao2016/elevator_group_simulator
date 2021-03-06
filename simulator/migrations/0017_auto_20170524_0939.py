# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-24 07:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simulator', '0016_auto_20170522_0922'),
    ]

    operations = [
        migrations.AddField(
            model_name='simulationdetails',
            name='arrivalRateEnd',
            field=models.FloatField(default=5),
        ),
        migrations.AddField(
            model_name='simulationdetails',
            name='arrivalRateStep',
            field=models.FloatField(default=1),
        ),
        migrations.AddField(
            model_name='simulationdetails',
            name='randomSeed',
            field=models.IntegerField(default=37),
        ),
        migrations.AlterField(
            model_name='simulationdetails',
            name='arrivalRate',
            field=models.FloatField(default=1),
        ),
    ]

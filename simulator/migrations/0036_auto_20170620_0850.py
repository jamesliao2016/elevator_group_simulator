# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-20 06:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simulator', '0035_statpassengers_entryfloor'),
    ]

    operations = [
        migrations.AddField(
            model_name='statsimulation',
            name='simulation_time',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='statsimulationsummary',
            name='simulation_time',
            field=models.FloatField(default=0),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-20 11:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simulator', '0041_auto_20170720_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmotioncycle',
            name='simulation',
            field=models.FloatField(default=0),
        ),
    ]
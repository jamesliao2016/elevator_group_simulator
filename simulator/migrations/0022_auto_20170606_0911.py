# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-06 07:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simulator', '0021_auto_20170602_1011'),
    ]

    operations = [
        migrations.CreateModel(
            name='Requirements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building_type', models.CharField(default=0, max_length=200)),
                ('rating', models.CharField(default=0, max_length=200)),
                ('AWT', models.FloatField()),
                ('AINT', models.FloatField()),
                ('ATTD', models.FloatField()),
                ('ACLF', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='building',
            name='author',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='building',
            name='type',
            field=models.CharField(default='Residential', max_length=200),
        ),
    ]

# pylint: skip-file
# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-03-27 15:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passive_data_kit', '0083_auto_20200324_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appconfiguration',
            name='context_pattern',
            field=models.CharField(db_index=True, default='.*', max_length=1024),
        ),
        migrations.AlterField(
            model_name='appconfiguration',
            name='id_pattern',
            field=models.CharField(db_index=True, max_length=1024),
        ),
    ]

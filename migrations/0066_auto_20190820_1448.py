# pylint: skip-file
# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-08-20 19:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passive_data_kit', '0065_devicemodel_reference'),
    ]

    operations = [
        migrations.AddField(
            model_name='deviceissue',
            name='platform',
            field=models.CharField(blank=True, max_length=1048576, null=True),
        ),
        migrations.AddField(
            model_name='deviceissue',
            name='platform_version',
            field=models.CharField(blank=True, max_length=1048576, null=True),
        ),
        migrations.AddField(
            model_name='deviceissue',
            name='user_agent',
            field=models.CharField(blank=True, max_length=1048576, null=True),
        ),
    ]

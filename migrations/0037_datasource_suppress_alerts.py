# pylint: skip-file

# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-05 21:59


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passive_data_kit', '0036_datasourcegroup_suppress_alerts'),
    ]

    operations = [
        migrations.AddField(
            model_name='datasource',
            name='suppress_alerts',
            field=models.BooleanField(default=False),
        ),
    ]

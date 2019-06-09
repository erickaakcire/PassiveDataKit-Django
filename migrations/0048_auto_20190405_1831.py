# pylint: skip-file
# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-05 22:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('passive_data_kit', '0047_auto_20190405_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datapoint',
            name='generator_definition',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='data_points', to='passive_data_kit.DataGeneratorDefinition'),
        ),
    ]

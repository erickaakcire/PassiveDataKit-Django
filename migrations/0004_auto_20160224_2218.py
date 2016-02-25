# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-24 22:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('passive_data_kit', '0003_auto_20160211_0223'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(db_index=True, max_length=1024)),
                ('name', models.CharField(db_index=True, max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='DataSourceGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=1024)),
            ],
        ),
        migrations.AddField(
            model_name='datasource',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sources', to='passive_data_kit.DataSourceGroup'),
        ),
    ]

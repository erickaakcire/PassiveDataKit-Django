# pylint: skip-file
# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-20 04:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('passive_data_kit', '0053_reportdestination'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='datapoint',
            index_together=set([('source', 'generator_identifier'), ('source', 'generator_identifier', 'secondary_identifier'), ('generator_identifier', 'recorded'), ('generator_definition', 'source_reference'), ('generator_identifier', 'secondary_identifier', 'recorded'), ('source', 'created'), ('generator_identifier', 'secondary_identifier'), ('source', 'generator_identifier', 'secondary_identifier', 'recorded'), ('source_reference', 'created'), ('source', 'generator_identifier', 'secondary_identifier', 'created'), ('generator_identifier', 'created', 'recorded'), ('source', 'generator_identifier', 'created'), ('generator_identifier', 'secondary_identifier', 'created'), ('source', 'generator_identifier', 'created', 'recorded'), ('generator_identifier', 'created'), ('generator_identifier', 'secondary_identifier', 'created', 'recorded'), ('source', 'server_generated'), ('source', 'generator_identifier', 'secondary_identifier', 'created', 'recorded'), ('source', 'user_agent'), ('source', 'generator_identifier', 'recorded')]),
        ),
    ]

# pylint: disable=line-too-long, no-member

import calendar
import csv
import datetime
import os
import tempfile
import time

from zipfile import ZipFile

import arrow

from django.template.loader import render_to_string
from django.utils import timezone
from django.utils.text import slugify

from ..models import DataPoint

WINDOW_SIZE = 300

def fetch_values(source, generator, start, end):
    values = []

    index = start
    current_value = None

    for point in DataPoint.objects.filter(source=source.identifier, generator_identifier=generator, created__gt=start, created__lte=end).order_by('created'):
        if (point.created - index).total_seconds() > WINDOW_SIZE:
            if current_value is not None and current_value['min_value'] != -1: # pylint: disable=unsubscriptable-object
                values.append(current_value)

            current_value = None
            index = index + datetime.timedelta(seconds=WINDOW_SIZE)

        if current_value is None:
            current_value = {
                'min_value': -1,
                'max_value': -1,
                'timestamp': time.mktime(index.timetuple()),
                'created': index,
                'duration': WINDOW_SIZE
            }

        properties = point.fetch_properties()

        for level in properties['sensor_data']['light_level']:
            if current_value['min_value'] == -1 or level < current_value['min_value']:
                current_value['min_value'] = level

            if current_value['max_value'] == -1 or level > current_value['max_value']:
                current_value['max_value'] = level

#        duration = properties['sensor_data']['observed'][-1] - properties['sensor_data']['observed'][0]
#        timestamp = properties['sensor_data']['observed'][0] + (duration / 2)
#
#        value['min_value'] = min_value
#        value['max_value'] = max_value
#        value['duration'] = duration / (1000 * 1000 * 1000)
#        value['timestamp'] = timestamp / (1000 * 1000 * 1000)
#        value['created'] = point.created
#
#        values.append(value)

    return values


def generator_name(identifier): # pylint: disable=unused-argument
    return 'Light Sensor'

def visualization(source, generator):
    context = {}
    context['source'] = source
    context['generator_identifier'] = generator

    end = timezone.now()
    start = end - datetime.timedelta(days=1)

    context['values'] = fetch_values(source, generator, start, end)

    context['start'] = time.mktime(start.timetuple())
    context['end'] = time.mktime(end.timetuple())

    return render_to_string('pdk_sensor_light_template.html', context)

def data_table(source, generator):
    context = {}
    context['source'] = source
    context['generator_identifier'] = generator

    end = timezone.now()
    start = end - datetime.timedelta(days=1)

    context['values'] = fetch_values(source, generator, start, end)

    return render_to_string('pdk_sensor_light_table_template.html', context)

def compile_report(generator, sources): # pylint: disable=too-many-locals
    filename = tempfile.gettempdir() + '/pdk_export_' + str(arrow.get().timestamp) + '.zip'

    with ZipFile(filename, 'w') as export_file:
        for source in sources:
            identifier = slugify(generator + '__' + source)

            secondary_filename = tempfile.gettempdir() + '/' + identifier + '.txt'

            with open(secondary_filename, 'w') as outfile:
                writer = csv.writer(outfile, delimiter='\t')

                columns = [
                    'Source',
                    'Created Timestamp',
                    'Created Date',
                    'Recorded Timestamp',
                    'Recorded Date',
                    'Raw Timestamp',
                    'Normalized Timestamp',
                    'Light Level',
                    'Accuracy'
                ]

                writer.writerow(columns)

                points = DataPoint.objects.filter(source=source, generator_identifier=generator).order_by('created')

                index = 0
                count = points.count()

                while index < count:
                    for point in points[index:(index + 500)]:
                        properties = point.fetch_properties()

                        if 'observed' in properties['sensor_data']:
                            for i in range(0, len(properties['sensor_data']['observed'])):
                                row = []

                                row.append(point.source)
                                row.append(calendar.timegm(point.created.utctimetuple()))
                                row.append(point.created.isoformat())

                                row.append(calendar.timegm(point.recorded.utctimetuple()))
                                row.append(point.recorded.isoformat())

                                row.append(properties['sensor_data']['raw_timestamp'][i])
                                row.append(properties['sensor_data']['observed'][i])
                                row.append(properties['sensor_data']['light_level'][i])
                                row.append(properties['sensor_data']['accuracy'][i])

                                writer.writerow(row)

                    index += 500

            export_file.write(secondary_filename, slugify(generator) + '/' + slugify(source) + '.txt')

            os.remove(secondary_filename)

    return filename

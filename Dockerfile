# Dockerfile
FROM quay.io/aptible/ubuntu:14.04

RUN apt-install software-properties-common
RUN add-apt-repository "deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main"

# Basic dependencies
RUN apt-install build-essential python-dev python-setuptools
RUN apt-install libxml2-dev libxslt1-dev python-dev

# PostgreSQL dev headers and client (uncomment if you use PostgreSQL)
RUN apt-install libpq-dev postgresql-client-9.5 postgresql-contrib-9.5

RUN easy_install pip

# Add requirements.txt ONLY, then run pip install, so that Docker cache won't
# bust when changes are made to other repo files
ADD requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt

RUN django-admin startproject pdk
ADD . pdk/passive_data_kit
ADD aptible_settings.py pdk/pdk/settings.py

WORKDIR /app/pdk
RUN python manage.py migrate
RUN python manage.py collectstatic

ENV PORT 3000
EXPOSE 3000


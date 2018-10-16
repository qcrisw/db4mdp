#!/bin/bash

#start postgres database server
. init-db.sh

#build tables structure
python db4mdp/manage.py makemigrations
python db4mdp/manage.py migrate

#import csv files into database
psql -h /tmp -U postgres -d postgres -p 5555 -a -f import.sql

python db4mdp/manage.py runserver 0.0.0.0:8000
 
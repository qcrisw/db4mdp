#!/bin/bash

#start postgres database server
#. init-db.sh

#build tables structure
python db4mdp/manage.py makemigrations --name testing

#because of the issues with docker not creating files on local host, I have written testing_migrations.py for any future
#migrations that need to be made. Basically how this works is for every new migrations file, change the name (to be specified
#in the name attribute above). Then change the name of the file in the below python file. (KEEP THE DIRECTORY THE SAME ONLY
#CHANGE THE FILE NAME WHICH IS THE LAST FILE IN THE OS.JOIN COMMAND). Then when the python code runs, it will give you the code
#written in the file as the container sees it. Copy this into a python script and name it is as desired (name is not important
#now but will be in the next step). In order for django to recognise this migration as something that needs to be applied, you
#will have to access the postgres database using pgadmin4, add a row to that database (django_migrations table within public schema)
#to specify that it needs to recognise this migration and apply it.

python db4mdp/testing_migrations.py

#python db4mdp/manage.py findstatic michael.png

#cd db4mdp/static
#ls

#the fake option will make django assume that you've migrated already. If it happens that there is anything
# even a small thing not migrated, then it will not migrate it because you used the fake option. I'd only use the
# fake option if I know for a fact that the only change was the table that django is complaining about and I do a
# sanity check to ensure that the table actually exists with the same name. My point is that if you have 2 changes and
# one of them is the create table which already exists, if you fake it then the second change will not take effect.

#python db4mdp/manage.py migrate tracking_analyzer This was just to separately migrate these tables while i was having
#issues with migrating mdp

#python db4mdp/manage.py install_geoip_dataset needed to work with the tracking analyzer and setting access by country thing


python db4mdp/manage.py migrate mdp
#I don't think it has to run all migrations like it used to do it earlier because now the online postgres server has been setup
#that has already made all the necessary migrations and now they dont need to be made again.
#python db4mdp/manage.py migrate mdp 0012_testing --fake

#python db4mdp/manage.py collectstatic

#This next command is not to be used during production unless during first run-time
#It will be used for creating a super-user to access the /admin url instead of hard-coding it into one of the app files
#Note that shifting the database online has made having to create the SU every time on server start up unnecessary.
#Modify from online server as necessary.

#python db4mdp/manage.py createsuperuser


#import csv files into database
#PGPASSWORD = K-amH6uOaHUrGDgztWZOxaDaSSnXzUJp
psql -h dumbo.db.elephantsql.com -U rzowhigs -d rzowhigs -p 5432 -a -f -w

python db4mdp/manage.py runserver 0.0.0.0:8000
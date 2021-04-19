#!/bin/bash


# append all migration
python manage.py --upgrade

# start service
python manage.py -r --host=0.0.0.0 --port=8000

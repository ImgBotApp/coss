#!/bin/sh

python manage.py migrate --noinput
gunicorn coss.wsgi:application -w 2 -b 0.0.0.0:${PORT:-8000} --log-file -

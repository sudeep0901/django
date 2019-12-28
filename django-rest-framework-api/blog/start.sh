#!/bin/sh
echo "Starting gunicorn python wsgi server"
exec gunicorn blog.wsgi:application --bind  0.0.0.0:8000 ---workers 3

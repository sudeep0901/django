#!/bin/bash
echo "Starting Gunicorn."
exec gunicorn blog.wsgi:application --bind 0.0.0.0:8000

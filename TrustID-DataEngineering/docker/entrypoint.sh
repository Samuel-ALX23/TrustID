#!/bin/sh
echo "Starting application..."
exec gunicorn --bind 0.0.0.0:5000 main:app
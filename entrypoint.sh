#!/bin/ash

echo "Apply database migrations"
python manage.py migrate


exec "$@" # execute a command that entry point provided. NOTE add an space after exec 
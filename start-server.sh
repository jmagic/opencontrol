#!/usr/bin/env bash
# start-server.sh
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
    (cd zenav; python manage.py createsuperuser --no-input)
fi
#(cd zenav; gunicorn zenav.wsgi --user www-data --bind 0.0.0.0:8010 --workers 3) &
(cd zenav; python manage.py runserver 0.0.0.0:8010)&
nginx -g "daemon off;"

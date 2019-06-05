release: python manage.py migrate --noinput
web: gunicorn main.wsgi —-log-file -
# worker: celery worker -A main.celery --loglevel=info --logfile=worker.log -B

release: python manage.py migrate
--no-input
web: gunicorn deployToHeroku.wsgi --log-file=-

# web: python manage.py runserver
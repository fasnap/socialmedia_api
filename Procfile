release: python3 manage.py makemigrations --no-input
release: python3 manage.py migrate --no-input
web: gunicorn social_media.wsgi:application --log-file -
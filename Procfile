release: python manage.py migrate && python manage.py compilemessages
web: gunicorn portfolio.wsgi:application
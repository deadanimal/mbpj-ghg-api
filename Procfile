web: gunicorn api.wsgi -w 4 --max-requests 100
worker: celery -A  api worker --concurrency=8 -Ofair
beat: celery -A api beat

FROM python:3.9-slim-buster

WORKDIR /app

ARG REQUIREMENTS_FILE
COPY ./requirements ./requirements
RUN pip install --no-cache-dir -r "./requirements/$REQUIREMENTS_FILE"

CMD python manage.py collectstatic --noinput && \
    python manage.py migrate && \
    gunicorn --bind :8080 --workers 3 meduza_light.wsgi:application

COPY . .
# Meduza Light


### Как запустить

1. Создайте файл `.env` в корневой папке проекта.

Пример содержимого файла `.env`:
```dotenv
DEBUG=on
DJANGO_SECRET_KEY=your-secret-key
DATABASE_URL=psql://meduza_user:password@127.0.0.1:5432/meduza_db
CACHE_URL=rediscache://127.0.0.1:6379/1
STATIC_ROOT=/Users/space_monkey/Projects/medusa-light/staticfiles/static/
MEDIA_ROOT=/Users/space_monkey/Projects/medusa-light/staticfiles/media/
ALLOWED_HOSTS=localhost,127.0.0.1
```
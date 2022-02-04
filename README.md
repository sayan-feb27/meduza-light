# Meduza Light


### Как запустить

1. Создайте файлы `.env` и `.db_env` в корневой папке проекта.

Пример содержимого файла `.env`:
```dotenv
DEBUG=off
DJANGO_SECRET_KEY=your-secret-key
DATABASE_URL=psql://meduza_user:password@127.0.0.1:5432/meduza_db
CACHE_URL=rediscache://redis:6379/1
STATIC_ROOT=/Users/space_monkey/Projects/medusa-light/staticfiles/static/
MEDIA_ROOT=/Users/space_monkey/Projects/medusa-light/staticfiles/media/
ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0
REQUIREMENTS_FILE=prod.txt
```

Пример содержимого файла `.db_env`:
```dotenv
POSTGRES_USER=postgres
POSTGRES_PASSWORD=password
POSTGRES_D=meduza_db
POSTGRES_CREATE_USER=meduza_user
POSTGRES_CREATE_USER_PASSWORD=password
DATABASE_URL=psql://${POSTGRES_CREATE_USER}:${POSTGRES_CREATE_USER_PASSWORD}@db:5432/${POSTGRES_D}
```

2. В терминале запустить команду `docker-compose up -d`.



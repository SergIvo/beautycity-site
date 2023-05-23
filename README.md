# BeautyCity

Сайт для записи в  сети салонов красоты. Код написан в учебных целях, в рамках курса по Python и веб-разработке на сайте [Devman](https://dvmn.org).

## Запуск

Для запуска сайта вам понадобится Python третьей версии.

Создайте виртуальное окружение и становите зависимости из файла `requirements.txt`:
```sh
python -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```

Создайте базу данных (в текущей версии используется база данных SQLite)
```sh
python3 manage.py migrate
```

Запустите разработческий сервер
```
python3 manage.py runserver
```

## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` в одной папке с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Доступны 3 переменные:
- `DEBUG` — дебаг-режим. Поставьте `False`, чтобы отключить отладочный режим на production-сервере.
- `SECRET_KEY` — секретный ключ проекта.
- `ALLOWED_HOSTS` — см [документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts).
- `DATABASE_URL` — ссылка, содержащая данные для подключения к базе данных [по одной из перечисленных схем](https://github.com/jazzband/dj-database-url#url-schema).

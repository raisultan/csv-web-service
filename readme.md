<br />

  <h1 align="center">CSV WEB SERVICE</h1>

## Содержание

* [Технические детали](#технические-детали)
* [Локальная установка](#локальная-установка)
  * [Пререквизиты](#пререквизиты)
  * [Установка](#установка)
* [Работа с сервисом](#работа-с-сервисом)
* [Администрирование](#администрирование)
* [Контакты](#контакты)


## Технические детали

* [Django](https://www.djangoproject.com/)
* [Django Rest Framework](https://www.django-rest-framework.org/)
* [PostgreSQL](https://www.postgresql.org/)
* [Docker](https://docs.docker.com/)
* [docker-compose](https://docs.docker.com/compose/)
* [Celery](https://docs.celeryproject.org/en/stable/)
* [Redis](https://redis.io/documentation)
* [Nginx](https://docs.nginx.com/)
* [Gunicorn](https://docs.gunicorn.org/en/stable/configure.html)


## Локальная установка

Перейдите в директорию проекта и запустите следующие команды в терминале:
```bash
docker build .
docker-compose build
```

Для запуска проекта используйте команду:
```bash
docker-compose up
```

Теперь вы можете запрашивать и отправлять данные с: http://127.0.0.1:8000/api/


## Работа с сервисом

### Загрузка данных на сервер:
Файл должен быть разрешения `.csv`.

Пример формата данных в файле:
```
customer,item,total,quantity,date
bellwether,Цаворит,612,6,2018-12-14 08:29:52.506166
resplendent,Сапфир,8502,6,2018-12-14 14:43:45.883282
buckaroo,Рубин,342,2,2018-12-15 15:00:59.858739
zygote4id3n,Яшма,264,3,2018-12-16 00:01:13.013713
nambypamby,Берилл,660,5,2018-12-16 01:58:57.047891
```
Загрузка файла на сервис для обработки осуществляется через http://127.0.0.1:8000/api/deal/upload/, куда выполняется POST запрос с полем 'file', в котором находится ваш `.csv` файл.

### Получение обработанных данных
Для получения обработанных данных нужно выполнить GET запрос на http://127.0.0.1:8000/api/deal/clients/


## Администрирование
Администрирование приложения осуществляется через панель администратора на http://127.0.0.1:8000/admin/

У вас есть возможность создать администатора камандой `docker-compose run app sh -c "python3 manage.py createsuperuser"`


## Контакты

Райсултан Каримов - ki.xbozz@gmail.com

Ссылка на проект: [https://github.com/Raysultan/csv-web-service](https://github.com/Raysultan/csv-web-service)

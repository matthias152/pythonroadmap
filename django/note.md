# Django
Docs: https://docs.djangoproject.com/en/2.2/intro/  
Django to framework pythona do web developmentu.

## Basics

Aby stworzyć nowy projekt:
```
django-admin startproject mysite
```
Stawiamy serwer przez komendę:
```
python manage.py runserver
```

## Apps
Django działa poprzez aplikacje webowe, aby stworzyć nową aplikacje:
```
python manage.py startapp polls
```
Każdą stworzoną aplikacje dodajemy do listy *INSTALLED_APPS* w pliku *settings.py*

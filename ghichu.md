pip install django

## Khởi tạo project

django-admin startproject site1

## Migrate

cd .\site1\
python .\manage.py migrate

## Start server

python .\manage.py runserver

## Tạo module

python .\manage.py startapp home

## Database mysql

-   Vào settings.py
    DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'site1',
    'USER': 'root',
    'PASSWORD': '',
    'HOST': 'localhost',
    }
    }

-   Cài package: pip install pymysql

## load asset

-   Thư mục asset:
    module_name
    -static
    -asset_module
    -css
    -js
    -images
    -plugins
    -icons
-   Vào settings.py
    STATIC_URL = "static/"

-   Đầu template
    {% load static %}
    <!DOCTYPE html>
    <html lang="en">

-   Link asset
<link href="{%static 'app/plugins/pg-calendar/css/pignose.calendar.min.css' %}" rel="stylesheet">

## Upload hình ảnh

-   image = models.ImageField(null=True, blank=True)
-   pip install pillow

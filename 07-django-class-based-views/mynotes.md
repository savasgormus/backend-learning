- python -m venv env
- .\env\Scripts\activate
- pip install -r requirements.txt
    requirements.txt :
        asgiref==3.5.0
        Django==4.0.1
        django-crispy-forms==1.14.0
        Pillow==9.0.0
        python-decouple==3.5
        sqlparse==0.4.2
        tzdata==2021.5
- django-admin startproject main .
- py manage.py migrate
- py manage.py runserver
- py manage.py startapp fscohort


- Class-based View nedir?
Bir request alan ve bir response return eden bir fonksiyon ya da classtır. Bu response bir resim, video ya da html template'i olabilir.

Class-based View'in farkı ise inheritance ile üzerinde bazı değişiklikler yapabilmemiz ya da mixin(aynı anda birden çok class'ı inheritance etmek) yapabiliriz.

Ayrıca python objelerini çağırabiliriz(attribute).

Aradaki temel fark şu: Function-based Viewlerde kontrol tamamen bizde ve herşeyi kendimiz yazıyoruz. Class-based Viewlerde ise inherit edeceğimiz viewlerle ilgili daha çok bilgi sahibi olmak gerekiyor ve üzerinde gerektiğinde değişiklik yapmamız gerekiyor.

- models.py:

modelimizi oluşturuyoruz:

# 
'''
from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    email = models.EmailField(max_length=154, unique=True, blank=True, null=True)
    phone = models.CharField(max_length=50, unique=True, blank=True, null=True)

    GENDER =(
        ("1", "Female"),
        ("2", "Male"),
        ("3", "Other"),
        ("4", "Prefer Not Say"),
    )

    gender = models.CharField(max_length=50, choices=GENDER)
    number = models.IntegerField(unique=True, blank=True, null=True)
    image = models.ImageField(upload_to="student/", default="avatar.png")

    def __str__(self):
        return f"{self.number} {self.first_name} {self.last_name}"
'''
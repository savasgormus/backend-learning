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

- views.py

homepage için class based bir view yazacağız. fakat önce TemplateView'ı django.views.generic.base'den import etmeliyiz. class based viewler, function viewlerden farklı olarak request değil TemplateView alırlar.

# Code
```py
from django.views.generic.base import TemplateView

class HomeView(TemplateView):
    template_name = 'fscohort/home.html'
```

- şimdi bunu urls.py dosyasına kaydedeceğiz.
# Code
```py
from .views import HomeView

path('', HomeView.as_view(), name="home"),
```































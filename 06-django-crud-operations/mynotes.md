python -m venv env
.\env\Scripts\activate
pip install django
pip install python-decouple
django-admin startproject main .
py manage.py migrate
py manage.py runserver
py manage.py startapp fscohort

CRUD nedir?
Create - Read - Update - Delete

----- kurulum aşaması -----

- fscohort/templates/fscohort içerisine bir base.html dosyası oluşturduk ve bu html dosyasına bootstrap bağladık: 
<!-- 
<!DOCTYPE html>
{% load static %}

<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />

    <link
      rel="stylesheet"
      href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/css/bootstrap.min.css"
      integrity="sha384-rwoIResjU2yc3z8GV/NPeZWAv56rSmLldC3R/AZzGRnGxQQKnKkoFVhFQhNUwEyJ"
      crossorigin="anonymous"
    />

    {% comment %}
    <link rel="stylesheet" href=" {% static 'fscohort/css/bootstrap.min.css' %}" />
    {% endcomment %}

    <link rel="stylesheet" href=" {% static 'fscohort/css/style.css' %}  " />

    <title>Document</title>
  </head>

  <body>
    {% comment %} {% include "users/navbar.html" %} {% endcomment %}
    <div style="margin-top: 100px; margin-bottom: 100px" class="container">

      {% block container %}{% endblock container %}
    </div>
    <script
      src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
      integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"
      crossorigin="anonymous"
    ></script>
    <script
      src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
      integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
      crossorigin="anonymous"
    ></script>
    <script
      src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
      integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
      crossorigin="anonymous"
    ></script>
    <script src="{% static 'fscohort/js/timeout.js' %}"></script>
  </body>
</html>
-->

- index.html'i oluşturduk ve base.html'i buraya extend ettik.

- fscohort/views.py dosyasına bu oluşturduğumuz index.html için bir view oluşturduk.

<!-- 
from django.shortcuts import render

def index(request):
    return render(request, 'fscohort/index.html')
-->

- main/urls.py dosyasına include yöntemi ile yeni bir path oluşturduk:

<!-- 
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('fscohort.urls'))
]
 -->

- fscohort/urls.py dosyasını oluşturduk ve index viewsimizi import ettikten sonra bir path oluşturduk:

<!-- 
from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='home')
]
 -->

- fscohort/models.py: basit bir model oluşturuyoruz ve bunu migrate işlemlerine tutuyoruz. daha sonra bu formu adminboard'da görmek için fscohort/admin.py dosyasına ekliyoruz.

<!-- 
from django.db import models

# Create your models here.

class Student(models.Model):
    first_name : models.CharField(max_length=30)
    last_name : models.CharField(max_length=30)
    number : models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    class Meta:
        verbose_name_plural = 'Öğrenciler'
-->

<!-- 
from django.contrib import admin
from .models import Student
# Register your models here.

admin.site.register(Student)
-->

database'imize admin panelinden birkaç öğrenci ekleyelim. şimdi READ işlemini yapacağız. yani database'imizden veriyi çekip template'imize yansıtacağız.(frontende göndereceğiz)

- fscohort/views.py
models'den Student'ı import ettikten sonra bir fonksiyon yazacağız. bir değişken oluşturduk ve bu Student objesinin bütün elemanlarını buraya atadık. bir context oluşturacağız. context dictionary yapısındaydı. isim olarak yine 'students' verdik ve value olarak yukarıda oluşturduğumuz student değişkenini atadıktan sonra return kısmını yazacağız.
return render(request, 'fscohort/student_list.html', context) ile bize return olarak neyi render edeceğini belirttik.

<!-- 
from .models import Student

def student_list(request):
    students = Student.objects.all()
    context = {
        "students" : students
    }
    return render(request,'fscohort/student_list.html',context)
 -->

render'ın ikinci parametresi olan student_list.html dosyasını template klasöründe oluşturacağız.

- fscohort/templates/fscohort/student_list.html
html dosyamızı oluşturduk. ilk işimiz base.html'i extend etmek olacak. daha sonra bir block oluşturacağız. block ismi base.html'de verdiğimiz isimle aynı olmak zorunda(container). block içerisinde görmek istediğimiz contexti yazıyoruz: {{ student }}

- fscohort/urls.py
template'imizi görebilmemiz için buna bir path oluşturmamız lazım. views'den student_list'i import edip urlpatterns içerisine bu path'i 'list/' linki ve 'list' ismi ile ekledik.

<!-- 
from django.urls import path
from .views import index, student_list

urlpatterns = [
    path('', index, name='home'),
    path('list/', student_list,name='list')
]
 -->

şimdi /list/ linkine girdiğimizde bize oluşturduğumuz öğrencileri query şeklinde görebiliyoruz. şimdi bu listeyi biraz düzenli hale getirelim.

- fscohort/templates/fscohort/student_list.html
bloğumuzun içerisine bir liste oluşturacağız ve for döngüsü kullanarak sıralı bir şekilde görünmesini sağlayacağız.
<!-- 
{% block container %}
    <ul>
        {% for student in students  %}
            <li>{{ student.number }} - 
                {{ student.first_name }} - 
                {{ student.last_name}}</li>
        {% endfor %}
    </ul>
{% endblock container %}
 -->




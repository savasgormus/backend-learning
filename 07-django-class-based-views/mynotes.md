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
# CODE
```python
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
```

modelimiz için bir gender alanı oluşturduk ve içerisine seçenekler ekledik. daha sonra gender için modelimizde bir choice attribute'u ile bu seçenekleri seçmek için bir yer oluşturduk. admin.py dosyasına bu modeli ekledik.

migrate işlemimizi yaptıktan sonra runserver dedik ve admin panelinde gördük.

- templates/fscohort klasörü içerisine base.html dosyasını oluşturduk. container isimli bir block oluşturduk. ayrıca home page'e dönmek için bir a tagi oluşturduk. href= "{% url 'home' %} dedik. bu daha sonra oluşturacağımız home.html dosyasına oluşturacağımız view için gerekli olacak.(name='home')

# CODE
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>CW FSCohort</title>
  </head>

  <body>
    <h1>
      <hr />
      <center>Clarusway</center>
      <hr />
    </h1>
    <a href="{% url 'home' %}">HOME</a>

    {% block content %} 
    {# Add some content here on your pages! #}
    {% endblock content %}
    
  </body>
</html>
```

- forms.py:
form.py dosyası sayesinde models içerisinde oluşturduğumuz tabloyu frontende yansıtacağız.

# CODE
```python
from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        models = Student
        fields = '__all__'
```

- şimdi sırasıyla crud işlemleri için tek tek view ve template oluşturup urls.py dosyasında path'e ekleyeceğiz. fakat öncesinde media dosyalarını yüklemek ve app'imiz için yazacağımız url'leri işlemek için main/urls.py'da bir işlem yapmamız gerekiyor:

# CODE
```python
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('fscohort.urls'))
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

- views.py:
home page ve student list için birer view oluşturalım. daha sonra bu 2 view için birer template ve url pathi ekleyeceğiz:

# CODE views.py
```python
from django.shortcuts import render
from .models import Student
# Create your views here.

def home(request):
    return render(request, 'fscohort.home.html')

def student_list(request):
    students = Student.objects.all()
    context = {
        'students' : students
    }
    return render(request,'fscohort/student_list',context)
```

- urls.py:
student_list ve home için oluşturduğumuz viewleri import ettik ve path'lerini ekledik:

# CODE urls.py
```python
from django.urls import path
from .views import home,student_list

urlpatterns = [
    path('', home, name="home"),
    path('student_list/', student_list, name="list"),
]
```

# CODE home.html
```html
{% extends 'base.html' %}
{% block container %}
<h2>
    <center>
        This is home page <br><hr>
        <a href="{% url 'list' %}">List</a>
        <a href="{% url 'add' %}">Add</a>
    </center>
</h2>
{% endblock container %}
```

# CODE student_list.html
```html
{% extends 'fscohort/base.html' %} 
{% block content %}
<h2>Student List</h2>
<ul>
  {% for student in students %}
  <a href="{% url 'detail' student.id  %}">
    <li>{{student}}</li>
  </a>
  {% endfor %}
</ul>
{% endblock content %}
```

































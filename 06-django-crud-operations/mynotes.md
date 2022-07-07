- python -m venv env
- .\env\Scripts\activate
- pip install django
- pip install python-decouple
- django-admin startproject main .
- py manage.py migrate
- py manage.py runserver
- py manage.py startapp fscohort

- CRUD nedir?
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
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    number = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    
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
html dosyamızı oluşturduk. ilk işimiz base.html'i extend etmek olacak. daha sonra bir block oluşturacağız. block ismi base.html'de verdiğimiz isimle aynı olmak zorunda(container). block içerisinde görmek istediğimiz contexti yazıyoruz: {{ students }}

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

----- CREATE -----

şimdi database'e veri girişi sağlayacağız fakat bunun için ilk önce bir form oluşturup render etmemiz gerekiyor.

- fscohort/forms.py
bu dosyayı oluşturduk. 2 şekilde form yapabiliriz. birinci yok yeni bir form oluşturup gereken alanları tek tek yazmak. ikinci yol ise zaten hali hazırda backend için kullandığımız model'den bir form oluşturmak.
django'dan forms'u models.py'dan da Student'ı import ettikten sonra bir class tanımlayarak formumuzu oluşturacağız:

<!-- 
from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        labels = {'first_name' : 'Adınız', 'last_name' : 'Soyadınız', 'number' : 'Numaranız'} 
-->

label içerisine görmek istediğimiz şekilde form alanlarını değiştirdik. yine dictionary formatında key, value alarak bunu düzenledik.
şimdi bu form için view yazma vakti.

- fscohort/views.py:
yine aynı şekilde bir fonksiyon oluşturarak (student_add ismini verelim) bir context oluşturacağız ve render edeceği parametreleri vereceğiz. daha sonra bu view için bir template ve url oluşturacağız.

<!-- 
from .forms import StudentForm

def student_add(request):
    form = StudentForm()
    context = {
        'form' : form
    }
    return render(request, 'fscohort/student_add.html', context)
 -->

- fscohort/templates/fscohort/student_add.html:

base.html'i extend ettikten sonra oradaki block'u oluşturduk(container). ve içerisine bir form ve submit butonu oluşturduk.
bu bir post işlemi olduğu için {% csrf_token %} girdik. bu djangonun güvenlik önlemi olarak aldığı bir kod. csrf token olmadan post işlemini yapamayız. daha sonra student_add için oluşturduğumuz context'i token'ın altına girdik  {{ form.as_p }} (form ismini vermiştik.).

- fscohort/urls.py

bu template'i frontende yansıtmak için bir path oluşturmalıyız. student_app'i viewsden import ediyoruz ve urlpatterns içerisine linkini veriyoruz.

<!-- 
from django.urls import path
from .views import index, student_add, student_list

urlpatterns = [
    path('', index, name='home'),
    path('list/', student_list,name='list'),
    path('add/', student_add, name='add')
]
 -->

şu haliyle hiçbir veri girişi yapamayız. gelen veriyi yakalayıp database'imize göndermek için bir işlem yapacağız:

-fscohort/views.py

http://127.0.0.1:8000/add/ adresine girdiğimizde GET methoduyla request gönderiyoruz ve sayfayı görüyoruz. Şimdi formu doldurup 'POST' metoduyla request göndereceğiz. student_add isimli viewimize bununla ilgili bir kontrol eklememiz gerekiyor:
      if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('list')
burada yaptığımız işlem şu şekilde açıklanabilir: eğer gelen request 'POST' ise 'form' değişkeni içerisine StudentForm'a gelen Post verilerini at. ve eğer form valid ise formu kaydet ve 'list' linkine redirect et.
<!-- 
def student_add(request):
    form = StudentForm()    
    print(request.POST)
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('list')
    context = {
        'form' : form
    }
    return render(request, 'fscohort/student_add.html', context)
-->

bu şekilde database'imize frontend tarafından veri girişi yapmış olduk.

----- UPDATE -----

- fscohort/views.py

update işlemi için oluşturacağımız view, diğerlerinden farklı olarak 2 parametre alıyor. birisi request, diğeri ise unique olan id.
daha sonra bu id ile database'den veri çekeceğiz ve update işlemini gerçekleştireceğiz.
StudentForm'dan gelecek spesifik veriyi belirtmek için yani değişikliği yapacağımız öğrenciyi instance=student ile belirttik.

<!-- 
def student_update(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)  
        if form.is_valid():
            form.save()
            return redirect('list')
    context = {
        'form' : form
    }
    return render(request, 'fscohort/student_update.html', context)
-->

- fscohort/templates/fscohort/student_update.html:

viewimizi oluşturduktan sonra ilgili html dosyamızı oluşturduk. base.htmli extend ettik ve container isimli bloğumuzun içerisine formumuzu koyduk.
csrf_token, context içinde görmek istediğimiz veri(views.py'da 'form' ismini vermiştik.) ve submit butonumuzu yerleştirdik.

<!-- 
{% extends 'fscohort/base.html' %}

{% block container %}
<h2>Student Update</h2>
<form action="" method="POST">
    {% csrf_token %}
    {{form.as_p}}
    <input type="submit" value="Update">
</form>

{% endblock container %}
-->

- fscohort/urls.py:

view ve template'imizi oluşturduk. sırada url'sini oluşturmak var. path'i oluştururken şuna dikkat etmeliyiz. update edeceğimiz veri bir id ile gelmek zorunda. 'update/<int:id>' şeklinde belirtmemiz gerekecek.

<!-- 
from .views import student_update
path('update/<int:id',student_update,name='update') 
-->

bu şekilde http://127.0.0.1:8000/update/3 adresini girdiğimizde unique id'si 3 olan öğrenci bize gelecek.

artık yapacağımız işlem create işlemi ile neredeyse aynı. tek fark request.POST yanında instance=student'ı almak.

      if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
        return redirect('list')

eğer instance = student parametresini eklemez ise create işlemi oluşturur. biz bu sayede var olan instance'ı değiştirebiliyoruz.

<!-- 
def student_update(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(instance=student)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('list')

    context = {
        'form': form
    }
    return render(request, 'fscohort/student_update.html',context) 
-->

----- DELETE -----

- views.py:
delete işlemi de 2 parametre alır. request ve id. Student objesinden id'yi alıyoruz ve eğer request 'POST' ise bu objeyi siliyoruz ve 'list' urlsine yönlendiriyoruz.
<!-- 
def student_delete(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('list')
    return render(request,'fscohort/student_delete.html')
 -->

- urls.py 
path('delete/<int:id>',student_delete,name='delete')'ı url patterns'e ekliyoruz.

- student_delete.html
<!-- 
{% extends 'fscohort/base.html' %}

{% block container %}
    <form action="" method="POST">
        <p>Are You Sure to delete {{student}} </p>
        {% csrf_token %}
        <input type="submit" value="Yes">
    </form>
    <a href="{% url 'list' %}">
        <button>No</button>
    </a>
{% endblock container %}
 -->

python -m venv env
.\env\Scripts\activate
pip install django
pip install python-decouple
pip freeze > requirements.txt
django-admin startproject main .
python manage.py migrate
python manage.py runserver
python manage.py startapp student
python manage.py createsuperuser

- form/settings.py içerisine oluştuduğumuz app'i kaydettik.
- yine form/settings.py içerisine media öğelerimizin yer alacağı klasörü belirttik:
<!-- 
import os

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/' 
-->

- student/models.py içerisine ilk modelimizi yazıyoruz.
<!--     
class Student(models.Model) :
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    number = models.IntegerField(blank=True, null=True)
    profile_pic = models.ImageField(blank=True, upload_to='profile_pics') 
-->
    admin panelinde oluşturduğumuz model'in düzgün görüntülenmesi için oluşturduğumuz class'a __str__(self) ekliyoruz:

        def __str__(self):
            return f'{self.first_name} {self.last_name}'

- terminale gidiyoruz ve profil fotoğrafını görüntüleyebilmemiz için pillow'u yüklüyoruz. oluşturduğumuz model database'e yeni bir veri eklediği için makemigrations ve migrate işlemlerini de yapacağız:

pip install pillow
pip freeze > requirements.txt
py manage.py makemigrations
py manage.py migrate

- app'imiz için bir template klasörü oluşturacağız ve içerisine bir html dosyası oluşturacağız.
html dosyamızı dolduralım:
<!--     
    <h1>Home Page</h1>

    <h3>Student App</h3>
 -->

şimdi student.html diye bir dosya oluşturalım ve içine basit bir form oluşturalım:
<!-- 
<form action="">
    <label for="">Student Name</label>
    <input type="text">
    <input type="submit" value="OK">
</form>
 -->

- bu oluşturduğumuz html sayfalarını student/views.py dosyasında view olarak render edeceğiz:
<!-- 
def index(request):
    return render(request, 'student/index.html')

def student_page(request):
    return render(request, 'student/student.html')
 -->

- viewlerimizi oluşturduk. şimdi bu 2 viewi projemiz olan forms içerisine include kullanarak urlpattern olarak eklemeliyiz.
forms/urls.py
<!-- 
from django.urls import include
from student.views import index

urlpatterns = [
    path('',index, name='index'),
    path('student/', include('student.urls'))
] -->

- urlpatternimizi ekledik fakat students içerisinde urls dosyası yok. şimdi bu dosyayı oluşturacağız ki yukarıda girdiğimiz kod redirect edebilsin:
student/urls.py
<!-- 
from django.urls import path
from .views import student

urlpatterns = [
    path('',student, name='student')
] 
-->

- templates/student/ içerisine base.html dosyası oluşturduk ve standart html sayfamızı yarattık (! tab). DOCTYPE ALTINA {% load static%} yazarak statik dosyaları yükleyebiliriz.
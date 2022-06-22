Django View nedir?

Python class ya da fonksiyonudur. Web request alır ve web response verir.bu response bir html sayfası olabilir, redirect olabilir, 404 hatası ya da bir resim olabilir.
Frontend ve backendi bağlayan bir logice sahiptir. Template(html sayfası) ya da model'ı kullanıcıya gönderir.
class based views djangonun kendi classlarından inherit ettiği yapılardır ve işimizi kolaylaştırır.

Django Templates nedir?

Djangonun frontendi diyebiliriz. HTML kodlarımızı olduğu yere django template denir. 
Programlama dili ile html'in karışımı şeklinde yazılır. buna django template language deniyor.


def tmp(request):
    context = {
        'title' : 'Django View',
        'dict' : {'django' : 'view'}
        'list_items' : [1,2,3,4]
    }
    return render(request, 'tmp.html', context)

    - variables {{}}
<body>
    {{title}} <br>
    {{dict.django}} <br>
    {{list_items.0}} <br>
</body>

    - tags {% %}
<body>
    {% for i in list_items %} {% if i == 2 %} 
    <p>Henry</p>
    {% else %} {{i}} <br>
    {% endif %} {% endfor %}       
</body>

    - filters {{ | }}
<body>
    {{ title | upper }} <br>
    {{ title | truncatechars:3 }} <br>
    {{ list_items | slice: ":2" }}
</body>

------------------------------------------------------------------------------

python -m venv env
.\env\Scripts\activate
pip install django
pip freeze > requirements.txt
django-admin startproject main .
python manage.py runserver
python manage.py startapp app

app'imizi settings.py'a ekledik.


- app/views.py:

django.http'den HTTPResponse'ı import ettik. ve bir view oluşturduk. bu view'i include kullanarak main/urls.py dosyası içerisine register edeceğiz. yine include kullanacağımız için app içerisine urls.py dosyası oluşturmamız gerekecek.
<!-- 
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Hello World</h1>')
-->

- main/urls.py:

oluşturduğumuz view'i önce include'u import ederek buraya girdik.
<!-- 
from django.urls import include

urlpatterns = [
    path('',include("app.urls"))
] 
-->

- app/urls.py:

bu dosyayı kendimiz oluşturduk. main/urls.py'ı kopyaladık ve buraya yapıştırdık. import include ve admin'e ihtiyacımız olmadığı için bu satırları sildik.
home isimli view'imizi aynı dosya yolu içerisinde olduğu için .views şeklinde import ediyoruz. daha sonra urlpatterns'i değiştireceğiz.

path('',home, name='home')
url yolu, viewin kendisi, view'e verdiğimiz isim(django template için kullanacağız)

<!-- 
from django.urls import path
from .views import home

urlpatterns = [
    path('',home, name='home')
]
 -->


- runserver dedik ve çalıştığını gördük.
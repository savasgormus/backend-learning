Django View nedir?

Python class ya da fonksiyonudur. Web request alır ve web response verir.bu response bir html sayfası olabilir, redirect olabilir, 404 hatası ya da bir resim olabilir.
Frontend ve backendi bağlayan bir logice sahiptir. Template(html sayfası) ya da model'ı kullanıcıya gönderir.
class based views djangonun kendi classlarından inherit ettiği yapılardır ve işimizi kolaylaştırır.

Django Template nedir?

Djangonun frontendi diyebiliriz. HTML kodlarımızı olduğu yere django template denir. 

Django Template Language nedir?
Model View Template'e entegre bir syntaxtır. Dinamik varible'ları görüntülememizi sağlar. ana elemanları şunlardır:
Variables, Tags, Filters, Comments
Özetle frontend tarafını interaktif hale getirir.

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

- app/views.py:

fonksiyonumuza print(request.user) ekledik. böylece hangi kullanıcı login olmuş konsolda görebileceğiz.

<!-- 
def home(request):
    print(request.user)
    return HttpResponse('<h1>Hello World</h1>')
 -->

print(request.GET)
print(request.COOKIES)
print(request.path)
print(request.method)
print(request.META)
gibi özellikleri kullanabiliriz.

yeni bir view oluşturalım. fakat bu sefer render(request,) ile yapacağız.
frontende request objesiyle beraber birazdan oluşturacağımız html dosyasını getirecek(render edecek). render import edildikten sonra app içerisine templates isimli bir klasör oluşturacağız ve az önce yazdığımız fonksiyon veriyi buradan çekecek.
templates klasörünün içerisine de şu an üzerinde çalıştığımız application ile aynı isimde bir klasör oluşturmamız gerekiyor. (örneğin birden fazla applicationumuz var) bu durumda templates/app klasörünü oluşturmamız gerekiyor.

<!-- 
def special(request):
    return render(request, 'app/special.html')
 -->


- app/templates/app/special.html

buraya basit bir html yazacağız fakat ek olarak django template language ile kayıtlı kullanıcıyı da göreceğimiz bişey ekleyeceğiz:

<h1>This is special page</h1>

{{ request.user }}

daha sonra bu html sayfasını görebilmek için urls.py'a eklemeliyiz ki görebilelim.

- app/urls.py

special.html sayfasını buraya kaydettik.

<!-- 
path('special/',special, name='special') 
-->

http://127.0.0.1:8000/special/ linkini tıkladığımızda yeni oluşturduğumuz template'i görüntüleyeceğiz.

- app/views.py

şimdi special isimli views'ımıza bir context ekleyelim:

    context = {
        'title': 'clarusway',
        'dict1': {'django': 'best framework'},
        'my_list': [2, 3, 4]
    }

render içerisine de contexti ekledik.

<!-- special'ın son hali:
def special(request):
    context = {
        'title': 'clarusway',
        'dict1': {'django': 'best framework'},
        'my_list': [2, 3, 4]
    }
    return render(request, 'app/special.html',context)
 -->

 - app/templates/app/special.html

az önce view'e eklediğimiz contexti şimdi burada görüntüleyelim.

{{ title }} ile context içerisindeki title'ı html sayfasına görebiliyoruz:
(variablelar)
<h2>The best bootcamp {{title | upper}}</h2> 
(ilk title context'den geliyor, ikincisi ise bütün harfler büyük olsun istediğimiz için - {{variable | filter }})

yine context içerisinden dict1'i görelim:

{{ dict1.django | title }} (buradaki title filter, başharfleri büyük olsun diye)

context içerisindeki my_list'i for döngüsüne sokup bütün sayıları tek tek alalım:
(tagler)
{% for i in my_list %}
    <li>{{ i }}</li>
{% endfor %}   - for döngüsünü bu şekilde bitiriyoruz.

{# #} ise comment yazmak için kullanılıyor. örneğin:
{# buraya bir comment giriniz #}
ya da
{% comment  %}
this is multiple
line comment
{% endcomment %}

django template sayfasında html yazıyoruz fakat html comment kullanmak tavsiye edilmez. çünkü sayfayı incele dediğimizde commentler görünür halde oluyor.
django commentler frontende gitmez. bu yüzden django comment kullanmalıyız.

-----------------------------------------------------------------------------

- Static files (images,JS,CSS)
Django kurduğumuzda static dosyaları düzenleyecek app ve statik dosyaların depolanacağı dosya yolu settings.py'da otomatik olarak belirtiliyor.

app klasörünün altına static isminde bir klasör oluşturacağız. djangonun otomatik kurduğu staticfiles appi (django.contrib.staticfiles) buraya yönlendirerek veri çekmemizi sağlayacak.

örneğin app/static/app içerisine style.css diye bir dosya oluşturduk ve bir backgroundcolor verdik.
oluşturduğumuz application ile aynı isimde tekrar klasör açtık ki birden fazla applicationumuz var ise karışıklık olmasın.
<!-- 
body {
    background-color: aqua;
}
 -->

django template'de bunu aktif hale getirmek için ise sayfanın en başına {% load static %} yazarak css dosyamızı çağıracağız. devamında ise normal css dosyasını linkler gibi head kısmına css dosyamızın ismini yazacağız fakat django tempate language şeklinde :
<!-- 
{% load static %}

<head>
    <link rel="stylesheet" href="{% static 'app/style.css' %}">
</head> 
-->

template'imize bir resim ekleyelim:

<!-- 
<img src="{% static 'app/kediler.jpeg' %}" alt="kediler" height='300'>
 -->

app
    | - static
        |  - app1
            | - css
            | - html
            | - js
        |  - app2
            | - css
            | - html
            | - js

app\static\app\kediler.jpeg => app\static kısmını django'nun kendi uygulaması hallediyor o yüzden dosya yoluna static 'app/kediler.jpeg' yazdık.

eğer applerin haricinde başka bir yerde staticfile arayacaksa şunu settings.py'a ekleyebiliriz:

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

ana klasöre static isminde bir klasör oluşturduk ve içerisine bir css dosyası oluşturduk.
terminale python manage.py findstatic style.css yazdığımızda bize nerede olduğunu söyledi.
python manage.py findstatic app/style.css dediğimizde ise app içerisindeki css dosyasını buldu.
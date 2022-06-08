- python -m venv env => ile enviorement'imizi oluşturduk. 

- env\Scripts\activate => scriptleri aktive ettik.

- pip install django => django kurulumunu yaptık.

- pip list => django ya da diğer eklentiler yüklü mü kontrol ettik.

- pip freeze > requirements.txt komutu ile env için yüklediğimiz paketleri gösteren bir dosya yarattık. böylece daha sonra bu projeyi indirdiğimizde otomatik olarak indirebiliriz.

- pip install -r requirements.txt ile bu paketleri indirebiliriz. ya da bir repodan proje çektiğimizde bu komut ile otomatik olarak gereken bütün paketleri ve uygun versiyonlarını indirebiliriz.

- django-admin startproject src . => projemizi oluşturduk. best practice "src" ya da "main"

- django project
    - app 1
    - app 2
    - app 3

- python manage.py startapp "xxx" => app'imizi oluşturuyoruz.

- python manage.py runserver => server'ı başlat.

https://www.toptal.com/developers/gitignore sitesinden django için bir gitignore içeriği oluşturduk ve .gitignore'un içerisine yapıştırdık.

--- --- --- --- ---

- --- --- --- src/settings.py : --- --- ---

oluşturduğumuz app'i INSTALLED_APPS'e ekledik.
 


- --- --- --- src/urls.py : --- --- ---

burası bizim ana santralimiz. oluşturduğumuz app'e(fscohort) include methodu kullanarak buradan yönlendireceğiz. (component mantığı)

from django.urls import include  >> includu import ettik.

urlpatterns = [
    path('',include('fscohort.urls'))
]

'' yolu ile fscohort içerisindeki urls dosyasına yönlendirdik.



- --- --- --- fscohort/views.py: --- --- --- 

urls.py'da tetiklemesi için bir fonksiyon yazacağız. önce HttpResponse'ı import edeceğiz sonra fonksiyonumuza geçeceğiz:
fonksiyonumuzu yazarken HttpResponse'ı auto import ettik.

from django.http import HttpResponse

def home(request):
    return HttpResponse("hello world")



- --- --- --- fscohort/urls.py: --- --- ---

öncelikle fscohort klasörü içerisine urls.py dosyasını oluşturduk. src/urls dosyasından kopya çekerek gereksiz satırları silip içeriğini oluşturabiliriz.

yukarıda home isimli bir fonksiyon oluşturduk. şimdi bunu import etmeliyiz.
daha sonra da urlpatterns'in içine bu fonksiyonu yerleştireceğiz.
not: name='' bölümü daha sonra templateler için kullanılacak. şu an için ihtiyacımız yok.

from .views import home

urlpatterns = [
    path('', home, name='home')
]


- özet:
browserda linki girdiğimizde önce src içerisindeki urls dosyasına bakacak. bu dosya bizi fscohort/urls.py'e yönlendiriyor. burada girmiş olduğumuz url linki bir fonksiyon tetikliyor. tetiklediği fonksiyon ise views içerisinde yazdığımız home isimli fonksiyon.
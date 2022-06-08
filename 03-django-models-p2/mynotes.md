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

<!-- ! --- --- --- src/settings.py : --- --- --- -->

oluşturduğumuz app'i INSTALLED_APPS'e ekledik.
 


<!-- ! --- --- --- src/urls.py : --- --- --- -->

burası bizim ana santralimiz. oluşturduğumuz app'e(fscohort) include methodu kullanarak buradan yönlendireceğiz. (component mantığı)


<!-- ? -->
from django.urls import include  >> includu import ettik.

urlpatterns = [
    path('',include('fscohort.urls'))
]

'' yolu ile fscohort içerisindeki urls dosyasına yönlendirdik.
<!-- ? -->


<!-- ! --- --- --- fscohort/views.py: --- --- ---  -->

urls.py'da tetiklemesi için bir fonksiyon yazacağız. önce HttpResponse'ı import edeceğiz sonra fonksiyonumuza geçeceğiz:
fonksiyonumuzu yazarken HttpResponse'ı auto import ettik.


<!-- ? -->
from django.http import HttpResponse

def home(request):
    return HttpResponse("hello world")
<!-- ? -->




<!-- ! --- --- --- fscohort/urls.py: --- --- --- -->

öncelikle fscohort klasörü içerisine urls.py dosyasını oluşturduk. src/urls dosyasından kopya çekerek gereksiz satırları silip içeriğini oluşturabiliriz.

yukarıda home isimli bir fonksiyon oluşturduk. şimdi bunu import etmeliyiz.
daha sonra da urlpatterns'in içine bu fonksiyonu yerleştireceğiz.
not: name='' bölümü daha sonra templateler için kullanılacak. şu an için ihtiyacımız yok.


<!-- ? -->
from .views import home

urlpatterns = [
    path('', home, name='home')
]
<!-- ? -->



- özet:
browserda linki girdiğimizde önce src içerisindeki urls dosyasına bakacak. bu dosya bizi fscohort/urls.py'e yönlendiriyor. burada girmiş olduğumuz url linki bir fonksiyon tetikliyor. tetiklediği fonksiyon ise views içerisinde yazdığımız home isimli fonksiyon.


<!-- ! --- --- --- fscohort/models.py --- --- --- -->

database içerisindeki tabloları oluşturduğumuz yer. tablolarımızı temsil eden yapılar ise class.
şimdi basit bir id, first_name, last_name ve number'dan oluşan bir student tablosu oluşturalım:



<!-- ? -->
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name =  models.CharField(max_length=50)
    number = models.IntegerField()
<!-- ? -->


- models.Model'den inherit ettik. yani Model'in bütün özelliklerini Student isimli class'ımız da alacak.
- id kısmını django bizim için kendisi oluşturuyor o yüzden diğer sütunlara geçelim:

models.Field Type ( Field Option )

- first_name models içerisindeki Charfield özelliğini aldık ve max karakter sayısını belirledik.
- last_name models içerisindeki Charfield özelliğini aldık ve max karakter sayısını belirledik.
- number models içerisindeki Integer özelliğini aldığımız için sadece sayı girilecek.


bu işlemleri database'e aktarmak için terminale 2 tane komut girmemiz gerekli:
- python manage.py makemigrations  : djangoya hazırlığını yapması için bu komutu veriyoruz ve gerekli scriptler çalışıyor. (migrations klasörü appimizin içerisinde otomatik olarak oluştu.)
- python manage.py migrate : bu komut ile de oluşturduğumuz tabloyu database'e ekliyor.


<!-- ! fscohort/admin.py -->

bu tabloyu admin paneline import ediyoruz.

<!-- ? -->
from .models import Student

admin.site.register(Student)
<!-- ? -->


şimdi bu oluşturduğumuz tabloyu admin panelinde görelim. önce superuser oluşturalım ve server'ımızı tekrar çalıştıralım:
- python manage.py createsuperuser
- python manage.py runserver
- http://127.0.0.1:8000/admin/


admin panelinde öğrenci eklediğimizde her eklediğimiz veriyi "Student object" olarak görüyoruz. şimdi bunu düzeltelim:

<!-- ! --- --- --- fscohort/models.py --- --- --- -->

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name =  models.CharField(max_length=50)
    number = models.IntegerField()

    def __str__(self):
        return self.first_name

yazdığımız fonksiyona yukarıdaki __str__ metodunu ekleyerek first_name'leri görürüz.



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

ya da biraz daha değiştirip fstring içerisine alıp isim soy isim olarak görelim:

    return (f"{self.first_name} {self.last_name}")

djangonun Meta özelliğini ekleyelim ve numaraya göre sıralama işlemi yapalım:

    class Meta:
        ordering = ["number"]   sıralama şekli
        verbose_name_plural = "Öğrenciler"  tablonun paneldeki görünen ismi

bu bilgilere django dökümanından ulaşabiliriz:
https://docs.djangoproject.com/en/4.0/topics/db/models/#meta-options


yaptığımız tabloyu sqlite extensionu ile görelim. db.sqlite3 dosyasında fscohort'u tıkladık ve show tables dedik.

--------------------------- Django ORM ve Query sets ------------------------------

- python manage.py shell komutunu girelim. consola şunları yazıyoruz:

- from fscohort.models import Student   database'e tablo girdik

- s1 = Student(first_name="John", last_name="Doe", number=123)   bir obje oluşturduk ve class olarak içini doldurduk.

- s1.save()  database'e bu veriyi girdik

- s2 = Student.objects.create(first_name="joe", last_name="Demaio", number=123)
bu şekilde ise save() metodunu kullanmadan direkt database'e bu veriyi girebiliriz.

https://docs.djangoproject.com/en/4.0/ref/models/querysets/


----------------- Field options--------------------------------

fscohort/models.py
oluşturduğumuz tabloya farklı özellikler ekleyelim
not: burada yaptığımız işlemler tabloda değişikliğe yol açacağı için istediğimiz eklemeleri yaptıktan sonra konsola makemigrations ve migrate komutlarını girmeliyiz.

about = models.Textfield(null=True, blank=True)
avatar = models.ImageField(null=True, blank=True, upload_to='media/') (media diye bir klasör oluşturup onun içine koyacak) 
not: bir resim yüklemek istiyor isek pythonun görüntüleme kütüphanesi Pillow'u yüklemeliyiz. (python -m pip install Pillow)

database'de resim vs depolama olmaz. size path'i verir.
bu resmi görmek için bazı ayarlamalar yapacağız:

    src/settings.py :
    STATIC_URL altına şunu ekliyoruz: MEDIA_URL = 'media/'

    src/urls.py :

        from django.conf import settings
        from django.conf.urls.static import static

        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


register_date = models.DateTimeField(auto_now_add=True)  => register olduğu tarih ve saat
update_date = models.DateTimeField(auto_now=True )  => değişiklik yaptığımızda girilen tarih ve saat

DateField ise sadece tarihi alır.
auto_now_add giriş için kullanıldı. tarih / saati aldı ve ekledi.
auto_now ise değişiklik yaptığımız tarih /saati aldı ve güncelledi.


şimdi Student class'ımızda YEAR_IN_SCHOOL_CHOICES isminde bir obje oluşturduk ve bir değişken ile bunu fonksiyonumuza ekledik. 

YEAR_IN_SCHOOL_CHOICES = [
        ("FR", 'Freshman'),
        ("SP", 'Sophomore'),
        ("JR", 'Junior'),
        ("SR", 'Senion'),
        ("GRD", 'Graduate'),
    ]
year_in_school = models.CharField(max_length=3, choices=YEAR_IN_SCHOOL_CHOICES)

bu oluşturduğumuz seçenekleri son eklediğimiz kod satırı ile seçebileceğiz.

formumuz değişikliğe uğrayacağı için yine makemigrations ve migrate işlemlerini uygulayacağız.
makemigrations işleminde bize bir soru gelecek. default(2)'yi seçtik.


------------------------- RELATIONSHIPS ----------------------


python manage.py startapp relations ile yeni bir proje oluşturduk ve src klasörü içerisindeki settings'e bu yeni appimizi ekledik.


relationship kavramı ile tabloları parçalar haline ayırırız. bunun bize sağladığı avantajlar ise :
    - daha sade ve anlaşılır bir yapı
    - daha küçük database boyutu
    - daha sade sorgular
    - daha hızlı response

djangoda 3 çeşit relationship vardır: one to one, many to one, many to many.

one to one:
    örneğin bir sosyal medya sitesine giriş yaptık. buradaki profil sayfası sadece 1 kişiye aittir.

relations/models içerisine 2 tane tablo oluşturalım ve bu tabloları relations/admin.py dosyası içerisine girelim, daha sonra da migrate işlemlerin gerçekleştirelim.
<!-- relations/admin.

from models import Creator, Language

admin.site.register(Creator)
admin.site.register(Language)
 -->


<!-- relations/models.py

class Creator(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name


class Language(models.Model):
    name = models.CharField(max_length=20)
    creator = models.OneToOneField(Creator, on_delete=models.CASCADE) 
 -->

one to one relationship kurduğumuzda 1 tablodan sadece 1 tane seçenek seçebiliriz.

onetoonefield içerisinde yazdığımız on_delete=models.CASCADE şu işe yarıyor. eğer bu opsiyon silinirse ona bağlı olan diğer tüm seçenekler silinsin.
on_delete=models.PROTECT ise silinmesini engeller.
on_delete=models.SET_NULL, null=true silindiğinde null verir.
on_delete=models.SET_DEFAULT, default=xxx silindiğinde default belirlediğimiz değeri verir.


many to one:

bir tablodaki obje, diğer tablodaki birden fazla objeye bağlanabilir. örneğin 1 doktorun birden fazla hastası olabilir. ya da bir blog düşünelim. bir kullanıcının birden fazla postu olabilir. ama bir postun 2 sahibi olamaz.
models.ForeignKey(bağlı olduğu tablo, on_delete metodu)

<!-- 
class Frameworks(models.Model):
    name = models.CharField(max_length=20)
    language = models.ForeignKey(Language, on_delete=models.PROTECT) 
    -->

many to many:
<!-- 
class Developers(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    frameworks = models.ManyToManyField(Frameworks)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
-->
on_delete modeli kullanmamıza gerek yok çünkü çoklu bir ilişki uyguluyoruz.
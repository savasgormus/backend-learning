- python3 -m venv env => ile enviorement'imizi oluşturduk. 
- env\Scripts\activate => scriptleri aktive ettik.
- pip install django => django kurulumunu yaptık.
- pip list => django ya da diğer eklentiler yüklü mü kontrol ettik.
- django-admin startproject src . => projemizi oluşturduk. best practice "src" ya da "main"

- django project
    - app 1
    - app 2
    - app 3

- python3 manage.py startapp "xxx" => app'imizi oluşturuyoruz.

- python3 manage.py runserver => server'ı başlat.

---------- src/settings.py ve urls.py 

- oluşturduğumuz app'i settings.py => INSTALLED_APPS'e ekledik.
- homepage oluşturacağız. fakat bunu urls.py dosyasına urlpatterns'a path olarak eklemeliyiz.

from django.urls.conf import include => ile include'u import ettik.

                path('', include('store.urls'))
path => standart
(
- '' => url linki, 
- include('store.urls') => app'in url'yi çekeceği yer. store içerisindeki urls.py dosyası
)


---------- store/views.py

- önce django.http'den HttpResponse'u import ettik ve bir fonksiyon ile (home) anasayfamızı oluşturduk.  

from django.http import HttpResponse
def home(request):
    return HttpResponse("Welcome to my store")


--------- store/urls.py

- store klasörü içerisine urls.py dosyası oluşturduk ve oluşturduğumuz view'i buraya tanıtıyoruz.

from django.urls import path
from .views import home(verdiğimiz isim)

urlpatterns = [
    path('', home)
]


---------- store/models.py

models.py'da oluşturacağımız her bir model, database'de bir tabloya denk geliyor.

örneğin: 
class Person(models.Model) :  
        <!-- bir tablo oluşturduk. tablonun ismi Person (models.Model ise standart bir kullanım) -->
    first_name = models.CharField(max_length=30)
        <!-- bu tablonun bir kolonunu oluşturduk. Charfield ile giriş yapacağımız datanın tipini belirledik ve max_lengt ile karakter sınırlaması sağladık -->
    number = models.IntegerField()
        <!-- yeni bir kolon oluşturduk ve bu kolonun türünü integer olarak belirledik. -->

basit Field tipleri:
    CharField()
    DataField()
    DecimalField()
    FileField()
    FloatField()
    BooleanField()
    ImageField()
    EmailField()
    DateTimeField()

basit Field Optionları:
    (null) default'ı False. True dersek giriş zorunlu olmaz.
    (blank) default'ı False. True dersek boş bırakılabilir.
    (db_column)
    (default)

biz bir model oluşturduk ve bunu djangoya bildireceğiz. bunun için şu komutu kullanıyoruz:
- python3 manage.py makemigrations store

database'e senkron etmek için ise şu komutu kullanıyoruz:
- python3 manage.py migrate

yaptığımız değişikliği eklemek için ise şu konumu kullanacağız:
- python3 manage.py makemigrations

models.py içerisinde her yaptığımız değişiklik için migrate etmemiz ve daha sonra database'e senkron etmemiz gerekir.


---------- admin.py ----------

djangonun bize sağladığı admin paneli. url sonunna /admin yazarak ulaşabiliriz.
kullanıcı adı ve şifresi oluşturmak için:
- python3 manage.py createsuperuser
daha sonra kullanıcı adı şifresi ve email'i belirttikten sonra bu panele ulaşabiliriz.

az önce oluşturduğumuz model'i adminboard'a import edeceğiz.

from store.models import Category
    <!-- aşağıdaki işlemi yapınca otomatik olarak import edecektir -->

admin.site.register(Category)
    <!-- admin.site.register standart bir kullanım (Category) ise store/models.py içerisinde oluşturduğumuz fonksiyonun ismi -->
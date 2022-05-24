python3 -m venv env => virtual enviorement'i oluşturduk
env\Scripts\activate => env.'i aktif hale getirdik
pip install django => django'yu kuruyoruz
django-admin startproject xxx . => django'yu proje ismi vererek başlatıyoruz
pyton manage.py runserver => server'ı açıyoruz
python manage.py startapp xxx => applicationumuza isim verdik ve çalıştırdık

bizi ilgilendiren 2 kısım var: 
    settings.py
    url.py


----- settings.py -----

SECRET_KEY bu olmadan django işlem yapamaz. verification için oldukça gerkeli.

ALLOWED_HOSTS hangi hostlarda işlem yapılabileceğini ayarlarız. sadece local ya da aldığımız domain gibi

INSTALLED_APPS yüklediğimiz paketleri buraya girmeliyiz ki çalıştıralım. aksi halde çalıştıramayız.

ROOT_URLCONF request geldiğinde yönlendireceği sayfa

DATABASES default olarak sqlite3 kullanıyor.

*** oluşturduğumuz app'i INSTALLED_APPS'e ekliyoruz.

---- views.py ----
önce HTTPResponse'u import ettik. daha sonra bir view oluşturacağız:

'''
def home(request):
    return HTTPResponse("Hello World")
'''
home view'ini oluşturduk. şimdi bunu .fscohor/urls.py dosyasına eklemeliyiz ki xxxx/home sayfasına girdiğimizde yukarıda oluştuduğumuz view'i görebilelim.

    --- urls.py ---

    önce student.views'den oluşturduğumuz home view'ini import ediyoruz:

from student.views import home
    
    daha sonra urlpatterns 'e oluştuduğumuz view'i path olarak ekliyoruz

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home,name="home"),     # 1. parametre url ismi, 2. view adı, 3. ismi
]
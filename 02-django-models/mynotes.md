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
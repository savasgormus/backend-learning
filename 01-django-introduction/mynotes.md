python3 -m venv env => virtual enviorement'i oluşturduk
env\Scripts\activate => env.'i aktif hale getirdik
pip install django => django'yu kuruyoruz
django-admin startproject xxx . => projeyi başlatıyoruz
pyton manage.py runserver => server'ı açıyoruz

bizi ilgilendiren 2 kısım var: 
    settings.py
    url.py


----- settings.py -----

SECRET_KEY bu olmadan django işlem yapamaz. verification için oldukça gerkeli.

ALLOWED_HOSTS hangi hostlarda işlem yapılabileceğini ayarlarız. sadece local ya da aldığımız domain gibi

INSTALLED_APPS yüklediğimiz paketleri buraya girmeliyiz ki çalıştıralım. aksi halde çalıştıramayız.

ROOT_URLCONF request geldiğinde yönlendireceği sayfa

DATABASES default olarak sqlite3 kullanıyor.


----- urls.py -----
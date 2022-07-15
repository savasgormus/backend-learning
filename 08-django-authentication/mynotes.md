- python -m venv env
- ./env/Scripts/activate
- pip install django
- pip install python-decouple
- python manage.py migrate
- python manage.py createsuperuser
- python manage.py runserver

# Authentication

- user, permission ve group modeli djangoda default olarak var. yani adminboard'a girdiğimizde bir kullanıcı ekleyebiliriz. temel attribute'lar username, password, email, first_name ve last_name. temel kullanımlar için yeterli.
- settings.py içerisindeki installed app'de bulunan django.contrib.auth ile bu yetkilendirmeyi otomatik olarak yüklüyor.











35
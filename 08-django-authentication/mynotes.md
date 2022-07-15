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

- şimdi admin panele girelim ve yeni bir kullanıcı oluşturalım. kullanıcı adı ve şifre için belirli bir format girmemiz gerekir. user oluşturduktan sonra şifreyi güvenlik önlemi gereği göremiyoruz çünkü sha256'ya uygun şekilde şifrelenmiş oluyor ve reverse engineerin yapmayı tamamen zorlaştırıyor. bir personel ya da yönetici bu şifreyi görüntüleyemez fakat değiştirebilir.

- şifreyi değiştirdiğimiz zaman kullanıcı bütün sessionlardan logout olur ve şifresinin değiştirildiğini bilebilir.

- Permission kısmında kullanıcıyı aktif ya da pasif konuma getirebiliriz. Staff status ile de admin girişi yetkisi verebiliriz.

- User permissions kısmında ise tek tek yetki verebiliriz. örneğin bütün izinleri verirsek superuser olur. ya da sadece belirli yerleri görüntüleme izni verebiliriz.

- Grup oluşturduğumuzda ise kullanıcı gibi gruba tek tek yetki verebiliriz. bir kullanıcı olarak çok fazla yetkiye sahip olabilir fakat farklı gruplarda da değişik yetkilere sahip olabilir. django bu konuda oldukça esneklik sağlayabiliyor.

# Programatik olarak kullanıcı ekleme

- terminal kullanarak kullanıcı oluşturmak. 
- yeni bir terminal açalım.
- python manage.py shell komutu ile shellimizi açıyoruz create_user() fonksiyonuyla kullanıcı ekliyoruz.
- create_user(username, email=None, password=None, **extra_fields) - aşağıdaki örnekte 2 farklı yöntemle kullanıcı oluşturacağız.

```py
from django.contrib.auth.models import User
user1 = User.objects.create_user('myusername', 'myemail@email.com', 'password')
user1.username #kullanıcı adını görüntüleyeceğiz
user2 = User.objects.create_user('Tuncay', last_name='T')
user2.last_name

user2.last_name = 'soyisim' #last_name'i değiştirdik.
user2.last_name     
user2.first_name = 'john'
user2.is_staff=True
user2.set_password('newpassword')
user2.save() # update ettikten sonra kaydediyoruz.
```

# Authentication ile kullanıcı ekleme








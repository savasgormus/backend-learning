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

# Authentication Views

- https://docs.djangoproject.com/en/4.0/topics/auth/default/#module-django.contrib.auth.views

- source klasörü içerisindeki urls.py dosyasına önce linkimizi ekliyoruz ve http://127.0.0.1:8000/accounts/ adresine gidiyoruz.
```py
urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
]
```
- bize 404 hatası verecek çünkü girmemiz gereken linkler accounts/ login/ accounts/ logout/ accounts/ password_change/ gibi url'lere girmemizi isteyecek. template'lerini hazırlamadığımız için hata almaya devam edeceğiz. fakat yukarıdaki işlem sayesinde tek tek login logout password gibi linkler için url pattern oluşturmamıza gerek kalmayacak.

- app/templates klasörünün içerisine register klasörü oluşturacağız. bu yaptığımız işlem default bir işlem olduğu için yine yukarıdaki kod sayesinde bağlantı kurabileceğiz. 'login.html' dosyası oluşturduk(bu isim de default) ve django dökümantasyonunda verdiği örneği içerisine atabiliriz. ya da daha basit bir örnek ile devam edelim ve http://127.0.0.1:8000/accounts/login/ linkine girelim:

- not: burada yazdığımız form'u django kendisi oluşturdu. biz bir form yazmadık.

```html
<h1>Login Page</h1>

{% block content %}

<form action="" method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Login">
</form>

{% endblock %}
```

- şu an basit bir login sayfası oluşturduk. şimdi oluşturduğumuz kullanıcılardan birisiyle giriş yapalım. karşımıza 404 hatası çıkacak çünkü http://127.0.0.1:8000/accounts/profile/ linkini oluşturmadık. bu djangonun defaultu fakat biz bunu değiştirebiliriz. örneğin giriş yaptıktan sonra homepage'e yönlendirelim.

- settings.py dosyası içerisine LOGIN_REDIRECT_URL = '/' ekleyerek login olduktan sonra otomatik olarak homepage'e yönlendirebiliriz. ya da urls.py dosyasında verdiğimiz name'i yazarak redirect işlemini yapabiliriz. Örneğin: LOGIN_REDIRECT_URL = 'home' . bu işlemi yaptıktan sonra tekrar giriş yapmayı deneyelim. homepage'e aktarılacağız.

- şimdi accounts/logout 'a bakalım. admin panelin'den çıkmışız gibi bir otomatik view gelecek. fakat gelen sayfada tekrar login linkine tıkladığımızda bizi admin girişine yönlendirmek isteyecek ve biz bunu istemiyoruz. yani kendimiz bir view yazmalıyız.

- http://127.0.0.1:8000/accounts/password_change/ adresine girelim. otomatik olarak bize djangonun password change sayfası gelecek.

- özetle bir çok template hazır geliyor fakat biz değişiklik yapabiliriz.

- hazır bir UserCreationForm kullanacağız. önce import edeceğiz daha sonra form'u hazırlayıp contextimize koyacağız ve de return render ile function base bir view oluşturacağız:

```py
views.py

from django.contrib.auth.forms import UserCreationForm

def register(request):
    form = UserCreationForm()
    context = {
        'form' : form
    }
    return render(request, "registration/register.html", context)
```

- sıradaki işlem bu view'i urls.py'a import edip urlpattern'e eklemek:

```py
from .views import register

urlpatterns = [
    path('register/', register, name='register'),
]
```

- registration/register.html template'ini oluşturduk ve içini basitçe dolduralım. ve http://127.0.0.1:8000/register/ adresine gidelim.

```html
<h1>Register Page</h1>

<form action="" method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Register">
</form>
```

- yine karşımıza djangonun otomatik olarak oluşturduğu form karşımıza geldi. fakat şu haliyle bir kullanıcı oluşturamayız. bu bir create işlemi olduğu için post ile gelen verilerin atamalarını yapacağız. fakat burada daha önemli bir kısım var. kullanıcı register olduğunda giriş yapmasını istiyoruz. o yüzden daha önceki örneklerde yaptığımız create işleminden farklı olarak bazı ek kodlar yazmamız gerekecek.


```py
from django.contrib.auth import login, authenticate

def register(request):
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # post ile veri geldi. eğer form valid ise kaydet
            # fakat authenticate için yeterli değil
            # aşağıda bu işlemi tamamlayacağız.

            # username ve password'u sayfadan çekiyoruz.
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            
            # yukarıdan çektiğimiz kullanıcı adı ve şifreyle user'ı oluşturduk ve authenticate işlemine tabi tuttuk.
            user = authenticate(username=username, password=password)
            
            # kullanıcının login olmasını istiyoruz ve bunun için de user gerekli.
            login(request, user)

            # login olduktan sonra anasayfaya redirect ediyoruz.
            return redirect('home')
            
    form = UserCreationForm()  
    context = {
        'form':form
    }
    return render(request, "registration/register.html", context)
```


 - Password change işlemi yapacağız. djangonun bizim için hazırladığı PasswordChangeView'i import edeceğiz. bu view class-based bir view olduğu için urls.py'da url pattern'e eklerken .as_view() fonksiyonu ile yazmamız gerekiyor. yine class-based view olduğu için bir view yazmamıza gerek yok. direkt urls.py'a import ederek kullanacağız. import kısmı biraz daha farklı. aşağıda göreceğiz:

 ```py
 - urls.py
from django.contrib.auth import views as auth_views

urlpatterns = [
   path('change-password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html'), name="change-password"),
]
 ```

- basit bir template hazırladık. yine kullandığımız form djangonun otomatik oluşturduğu bir change password formu olarak bize gelecek.

```html
<h2>Password change page</h2>

<form action="" method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Change Password">
</form>
```

- şifre değiştirdikten sonra yine bizi admin panelin şifre değiştirme sayfasına benzer bir sayfaya yönlendirecek. eğer istersek bunu da override edebiliriz. auth_views.PasswordChangeDoneView.as_view() içerisine template_name yazıp yeni bir template oluşturarak bunu yapabiliriz.

- Password reset işlemi yapacağız:
- bu işlem 4 sayfayı içeriyor. reset isteği, e mail gönderme, e mail'e tıklayınca açacağımız sayfa ve reset işlemi.
- yine class-based view'ımızı urls.py'a ekliyoruz. yukarıdaki işlemde auth_views'ı import ettiğimiz için tekrar bişey import etmemize gerek yok.

```py
urlpatterns = [
path('reset-password/', auth_views.PasswordResetView.as_view(template_name='registration/reset-password.html'), name="reset-password"),
]
```

- şu haliyle password reset işlemi yapamayız. ConnectionRefusedError at /reset-password/ diye bir hata alacağız. çünkü mail-backend'i oluşturacağız.
- consele back'endi oluşturmak için settings.py'a şunu ekleyeceğiz:
```py
- settings.py

EMAIL_BACKEND = 'django.core.mail.backends.consele.EmailBackend'
```

- bu işlemi yaptıktan sonra reset için e mail gönderdiğimizde terminalimizde bir e posta gönderisi alacağız. şu an console e mail backendimizi kurmuş olduk.
- bu email'de bize bir link verecek ve bu linke tıkladığımızda bizi password reset'in diğer adımı olan yeni şifre girme sayfasına yönlendirecek. şifremizi burada değiştirdiğimizde de reset/done yani sonuncu aşamaya gönderecek.
- yine bu sayfalar admin paneli sayfası gibi görüntülenecek. hazır class-based viewslerle yukarıdaki örneklerde olduğu gibi modifiye edebiliriz.

- logout işlemi de login işlemi gibi istediğimiz şekilde redirect edebiliriz. settings.py'a ekleyeceğimiz satır ile belirttiğimiz sayfaya geçiş yapacaktır.

```py
- settings.py
LOGOUT_REDIRECT_URL = 'home'
```


- Login required decorator

- bu işlemin amacı belirli bir sayfayı sadece login olmuş kullanıcıların görmesini sağlamak. view'imize bu decorator'ı import edeceğiz ve decorator kullanacağımız view'in üstüne @login_required yazacağız:

```py
- views.py

from django.contrib.auth.decorators import login_required

@login_required
def special(request):  
    return render(request, "user_example/special.html")
```

- kodumuzu bu şekilde düzenledikten sonra bahsi geçen sayfaya girmek istediğimizde eğer login olmadıysak bizi login sayfasına yönlendirecek.
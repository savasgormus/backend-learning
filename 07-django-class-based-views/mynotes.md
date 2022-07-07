- python -m venv env
- .\env\Scripts\activate
- pip install -r requirements.txt

    requirements.txt :
        asgiref==3.5.0
        Django==4.0.1
        django-crispy-forms==1.14.0
        Pillow==9.0.0
        python-decouple==3.5
        sqlparse==0.4.2
        tzdata==2021.5

- django-admin startproject main .
- py manage.py migrate
- py manage.py runserver
- py manage.py startapp fscohort


- Class-based View nedir?
Bir request alan ve bir response return eden bir fonksiyon ya da classtır. Bu response bir resim, video ya da html template'i olabilir.

Class-based View'in farkı ise inheritance ile üzerinde bazı değişiklikler yapabilmemiz ya da mixin(aynı anda birden çok class'ı inheritance etmek) yapabiliriz.

Ayrıca python objelerini çağırabiliriz(attribute).

Aradaki temel fark şu: Function-based Viewlerde kontrol tamamen bizde ve herşeyi kendimiz yazıyoruz. Class-based Viewlerde ise inherit edeceğimiz viewlerle ilgili daha çok bilgi sahibi olmak gerekiyor ve üzerinde gerektiğinde değişiklik yapmamız gerekiyor.

- views.py

homepage için class based bir view yazacağız. fakat önce TemplateView'ı django.views.generic.base'den import etmeliyiz. class based viewler, function viewlerden farklı olarak request değil TemplateView alırlar.

# Code
```py
from django.views.generic.base import TemplateView

class HomeView(TemplateView):
    template_name = 'fscohort/home.html'
```

- şimdi bunu urls.py dosyasına kaydedeceğiz.
# Code
```py
from .views import HomeView

path('', HomeView.as_view(), name="home"),
```

ikinci bir yöntem ise view'e yazmadan direkt urls.py'dan çekebiliriz. urls.py'a TemplateView'ı import ediyoruz ve oluşturduğumuz path içerisindeki TemplateView.as_view() fonksiyonuna html dosyasının adını yazıyoruz.

# Code
```py
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name = 'fscohort/home.html'), name="home"),
]
```

- List Views: objelerin listesini çağırmaya yarar. query set olarak bize getirir. 

from django.views.generic.list import ListView ile import ettik.
classımızı yazmaya başladık. öncelikle model'imizi belirtmemiz gerekiyor. template_name ile template ismimizi yazacağız fakat bizim oluşturduğumuz template generic bir isim olduğu için gerek yok. (fscohort/student_list.html)
context_object_name = 'students' olarak belirttik çünkü isim generic değil. html dosyasına gittiğimizde for döngüsünde student in students var. eğer html dosyamızın içerisindeki obje student_list olsaydı bu adımı da atlayabilirdik.
paginate_by = 10 ile de bir sayfa içerisinde kaç tane sonuç göreceğimizi belirledik(örneğin bir alışveriş sayfası hazırladık).

şimdi bunu urls.py dosyasında belirteceğiz.

StudentListView'i import ettik ve path içerisine .as_view() fonksiyonuyla bağladık.

# Code
```py
views.py
from django.views.generic.list import ListView

class StudentListView(ListView):
    model = Student
    context_object_name = 'students'
    paginate_by = 10

urls.py
from .views import StudentListView

urlpatterns =[
    path('student_list/', StudentListView.as_view(), name="list"),
]
```

- Detail Views:

from django.views.generic.detail import DetailView'i import ettik. Viewimizin modelini belirtiyoruz. burada ufak bir fark var. func based viewimize baktığımızda biz bunları id ile çektik. defaultu pk olarak geçiyor. pk'i id olarak modifiye edeceğiz: pk_url_kwarg = 'id'

yine aynı şekilde urls.py dosyasına import edip giriş yapıyoruz:
path('student_detail/', StudentDetailView.as_view(), name="list"),

# Code
```py
class StudentListView(ListView):
    model = Student
    context_object_name = 'students'
    paginate_by = 10
```

- Editin Views (Create, update, delete)

- Create View:

Bir obje oluşturur ve validasyon hataları varsa gösterir yoksa kaydeder.
django.views.generic.edit'den import ediyoruz.
model'imizi ve form_class'ımızı belirttikten sonra (çünkü model'i form'a çevirdik) template_name'imizi ekliyoruz. son işlemimiz ise redirect edeceğimiz yeri belirtmek. django.urls'den reverse_lazy'yi import ettiten sonra viewimize success_url = reverse_lazy('list') ile kayıt işlemi sonrası bize redirect edeceği template'i belirttik(urls.py'da verdiğimiz name'i yazıyoruz linki değil). urls.py dosyasına da bu oluşturduğumuz view'i (StudentCreateView.as_view()) pattern'e ekliyoruz.

# Code
```py
views.py

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'fscohort/student_add.html'
    success_url = reverse_lazy('list')

urls.py
from .views import StudentCreateView,

urlpatterns = [
    path('student_add/', StudentCreateView.as_view(), name="add"),
]
```

- Update View:

Create view ile aynı işe yarar fakat sadece var olanı değiştiriyor.
from django.views.generic.edit import UpdateView ile import ettik ve yine create ile aynı işlemleri uygulamaya devam ediyoruz. success_url için '/student_list/' diyerek direkt template yolunu yazdık fakat bu çok yaygın bir kullanım değil. ileride değişiklik yapmak istediğimizde bizim için problem yaratabilir. o yüzden best practice reverse_lazy() kullanmak.
tekrar urls.py'da bu viewimizi import edip urlpatterns içerisine path belirtiyoruz. fakat int:id yerine default olan pk kullanacağız. eğer id olarak kullanmak isteseydik pk_url_kwarg = 'id' diye viewimizde belirtmeliydik.

# Code
```py
views.py
from django.views.generic.edit import UpdateView
class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'fscohort/student_update.html'
    success_url = '/student_list/'

    
urls.py
from .views import StudentUpdateView
urlpattern = [
    path('update/<int:pk>/', StudentUpdateView.as_view(), name="update"),
]
```   



























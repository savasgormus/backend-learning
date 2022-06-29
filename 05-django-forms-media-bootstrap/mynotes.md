python -m venv env
.\env\Scripts\activate
pip install django
pip install python-decouple
pip freeze > requirements.txt
django-admin startproject main .
python manage.py migrate
python manage.py runserver
python manage.py startapp student
python manage.py createsuperuser

- form/settings.py içerisine oluştuduğumuz app'i kaydettik.
- yine form/settings.py içerisine media öğelerimizin yer alacağı klasörü belirttik:
<!-- 
import os

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/' 
-->

- student/models.py içerisine ilk modelimizi yazıyoruz.
<!--     
class Student(models.Model) :
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    number = models.IntegerField(blank=True, null=True)
    profile_pic = models.ImageField(blank=True, upload_to='profile_pics') 
-->
admin panelinde oluşturduğumuz model'in düzgün görüntülenmesi için oluşturduğumuz class'a __str__(self) ekliyoruz:

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

- terminale gidiyoruz ve profil fotoğrafını görüntüleyebilmemiz için pillow'u yüklüyoruz. oluşturduğumuz model database'e yeni bir veri eklediği için makemigrations ve migrate işlemlerini de yapacağız:

pip install pillow
pip freeze > requirements.txt
py manage.py makemigrations
py manage.py migrate

- app'imiz için bir template klasörü oluşturacağız ve içerisine bir html dosyası oluşturacağız.
html dosyamızı dolduralım:
<!--     
    <h1>Home Page</h1>

    <h3>Student App</h3>
 -->

şimdi student.html diye bir dosya oluşturalım ve içine basit bir form oluşturalım:
<!-- 
<form action="">
    <label for="">Student Name</label>
    <input type="text">
    <input type="submit" value="OK">
</form>
 -->

- bu oluşturduğumuz html sayfalarını student/views.py dosyasında view olarak render edeceğiz:
<!-- 
def index(request):
    return render(request, 'student/index.html')

def student_page(request):
    return render(request, 'student/student.html')
 -->

- viewlerimizi oluşturduk. şimdi bu 2 viewi projemiz olan forms içerisine include kullanarak urlpattern olarak eklemeliyiz.
forms/urls.py
<!-- 
from django.urls import include
from student.views import index

urlpatterns = [
    path('',index, name='index'),
    path('student/', include('student.urls'))
] -->

- urlpatternimizi ekledik fakat students içerisinde urls dosyası yok. şimdi bu dosyayı oluşturacağız ki yukarıda girdiğimiz kod redirect edebilsin:
student/urls.py
<!-- 
from django.urls import path
from .views import student

urlpatterns = [
    path('',student, name='student')
] 
-->

- templates/student/ içerisine base.html dosyası oluşturduk ve standart html sayfamızı yarattık (! tab). DOCTYPE ALTINA {% load static%} yazarak statik dosyaları yükleyebiliriz. Component yapısını kullanacağız. body içerisine bir container oluşturacağız:
    {% block container %}
    {% endblock %}  -- açtığımız bloğu kapatmamız gerekiyor
şeklinde bir block oluşturduk.

- index.html: bu oluşturduğumuz base.html dosyasını extend edeceğiz.
<!-- 
{% extends 'student/base.html' %}

{% block container %}
<h1>Home Page</h1>

<h3>Student App</h3>
{% endblock container%}
 -->
şimdi index html içerisinde container içerisine aldığımız satırları base.html'de oluşturduğumuz container isimli block içerisinde gösterecek. React'da kullandığımız componentler gibi. yani bizim asıl dosyamız base.html olacak. örneğin bir navbar yazacağız. tek tek her sayfa için yapacağımıza base.html'e yazarız ve tüm uygulamada sabit kalır. böylece modüler bir yapı sağlamış olacağız.

- aynı işlemi student.html dosyası için de yapacağız. base.html container içerisine burada veri çekecek.
<!-- 
{% extends 'student/base.html' %}

{% block container%}
<form action="">
    <label for="">student name</label>
    <input type="text" />
    <input type="submit" value="OK" />
</form>
{% endblock container %}
 -->

özet: student ve index html sayfalarını base.html'e extend ettik. yani birbirine bağladık. base.html sayfası içerisinde container ismini verdiğimiz block elementi gördüğü zaman bu iki sayfadan veri çekecek ve container bloğumuzun içerisine yansıyacak.
/student/ sayfasına girelim ve incele diyelim: görüldüğü gibi student sayfası base.html içerisindeki body'ye dahil. örneğin body içerisine bir div oluşturalım ve container bloğumuzu bu div içerisine alalım. değişikliği bu şekilde daha rahat görebiliriz. views içerisinde yazdığımız render fonksiyonu django template olarak yazdığımız bu dosyaları bize html dosyası olarak çeviriyor.

------------- forms ----------------

student/models içerisinde bir bir database table tanımlamıştık. django bize diyor ki tek tek bunları yapmakla uğraşmak yerine ben senin için yapabilirim. şimdi student klasörü içerisine forms.py diye bir dosya oluşturalım:

burada herşeyi kendimiz tasarlayıp bir form oluşturabiliriz. ya da bir model ile ilişkilendirip bir form oluşturabiliriz.

<!-- 
from django import forms

class StudentFormSimple(forms.form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    number = forms.IntegerField(required=False)
 -->
bu yaptığımızın aynısını zaten models.py dosyasında da yapmıştık. tek tek yeniden yazmak yerine model ile ilişkilendireceğiz:
forms.py:
<!-- 
from .models import Student

class StudentFrom(forms.ModelForm): 
    class Meta:
        model = Student
        fields = '__all__'
-->

- views.py dosyasına gidiyoruz: student_page içerisine bu formu koyacağız ve bir context oluşturacağız. context dictionary yapısındaydı. daha sonra da render'in 3. parametresi olarak bu contexti gireceğiz.

<!-- 
from .forms import StudentForm

def student_page(request):
    form = StudentForm()
    context = {
        'form' : form
    }
    return render(request, 'student/student.html',context) 
    -->

form = StudentForm() ile bir değişkene atadık sadece. bunu yapmadan context içerisinde oluşturduğumuz item'a StudentForm() da diyebilirdik:

context = {
    'form' : StudentForm()
}

burada en kritik nokta context içerisinde kullandığımızı birebir şekilde template içerisinde kullanabiliriz.(form değişebilir istediğimiz ismi verebiliriz fakat context içerisindeki 'form' ile template'e koyacağımız form ismi birbirini tutmalı.)

- templates/student/student.html: buradaki önceden oluşturduğumuz formu commente aldık. şimdi forms.py dosyasında oluşturduğumuz formu burada göstereceğiz.
önemli bir detay. bizim oluşturduğumuz form içerisinde resim yükleme özelliği var ve çalışması için form taginin içerisine şunu eklememiz gerekiyor: enctype='multipart/form-data'
formumuzu oluşturduk ve içerisine değişken gireceğimiz için {{}} kullanarak {{ form.as_p }} yazdık. submit butonumuzu da ekledik.
<!-- 
<form action="" method='POST' enctype='multipart/form-data'>

    {{ form.as_p }}
    <input type="submit" value="OK">
</form> -->

sayfamızı yenilediğimizde /student/ linki forms.py'da oluşturduğumuz formu sergileyecek.

özet:
models.py'da database'e işlenecek bir form oluşturmuştuk. daha sonra bunu forms.py dosyası içerisinde fields = '__all__' ile bütün veri girişlerini alacak şekilde tekrar oluşturduk çünkü frontend tarafında görmek istiyoruz.

daha sonra views.py'a gittik ve bu formdan 'form' isminde bir instance türettik. boş bir form olduğu için içerisine bir context ekledik ve template'e gönderdik.

template'in içerisinde formu yeniden tanımladık. {{form.as_p}}
burada kullandığımız .as_p'nin amacı her bir field'a p tagi ekliyor. böylece bize daha güzel bir görüntü oluşturuyor. 

- forms.py: 
burada fields = '__all__' demiştik. şimdi diğer opsiyonlarımızı görelim:
örneğin 
fields = ['first_name', 'last_name'] dediğimizde sadece isim ve soyisim kısmını göreceğiz.
ya da label isimlerini değiştirebiliriz.
labels = {'first_name' : 'User Name'} dictionary yapısı ile first_name'e atadığımız ismi 'User Name' olarak değiştirdik.

bu oluşturduğumuz formu doldurup göndermek istediğimizde bir hata alacağız. django güvenlik önlemi olarak csrf_token istiyor. biz bunu eklemediğimiz için işlem başarısız olacak.

- student/student.html dosyamıza formumuzu eklemiştik. şimdi buraya form içerisine eksik olan csrf_token'ımızı ekliyoruz:
<!-- 
<form action="" method='POST' enctype='multipart/form-data'>
    {% csrf_token %}
    {{ form.as_p }}
    
    <input type="submit" value="OK">
</form> -->

bu işlemi gerçekleştirdikten sonra konsolda 'POST' işleminin başarılı olduğunu göreceğiz.

- student/views.py
şimdi 
form = StudentForm(request.Post or None) dedikten sonra formun valid olup olmadığını anlamak için bir if statement oluşturacağız ve cleaned_data yöntemi ile form içerisindeki bilgiler konsolda göreceğiz:
<!-- 
def student_page(request):
    form = StudentForm(request.POST or None)

    if form.is_valid():
        form.save()
        print(form.cleaned_data.get('first_name'))
    context = {
        'form' : form
    }
    return render(request, 'student/student.html',context) 
    -->
form validasyonu nedir? 
örneğin username'i boş bıraktık. form'u kaydedemeyiz fakat space ile boşluk bırakarak frontendi kandırmaya çalışabiliriz. is_valid() ile bu seçeneği de ortadan kaldırırız. çünkü bu sayede backend tarafı modellere bakıyor ve tek tek kontrol ediyor. validasyon tamamlandıktan sonra form.save() ile backende gönderiyor. admin dashboard ya da db.sqlite3 dosyasında işlemin gerçekleşip gerçekleşmediğini görebiliriz.

admin dashboard ile görmeyi deneyelim:
açtığımızda göremeyeceğiz çünkü admin.py dosyasına bu tabloyu eklemedik. ekledikten sonra student isimli tablomuz adminboard'da yerini alacak:
<!-- 
from .models import Student

admin.site.register(Student) 
-->

özet:

views.py dosyasında oluşturduğumuz form'da eğer request post ise bilgilerini içine koyuyoruz ve validasyon sağlandıktan sonra kaydediyor.

- student/views.py
sorun: post işlemi ile kaydettikten sonra sayfa aynı kalıyor. yani aynı kullanıcı bilgisini arka arkaya kaydedebiliriz. başka bir sayfaya yönlendirmemiz lazım.
bunun için redirect'i import kullanmalıyız ve hangi sayfaya yönlendireceğimizi belirteceğiz.

form.save() işleminden hemen sonra return redirect('index') => buradaki 'index' urls.py dosyasında name=''e verdiğimiz parametre olmak zorunda.

<!-- 
def student_page(request):
    form = StudentForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('index')
        # print(form.cleaned_data.get('first_name'))
    context = {
        'form' : form
    }
    return render(request, 'student/student.html',context)
 -->

buraya kadar yaptığımız bütün işlemler yükleyeceğimiz resmi dahil etmedi. şimdi ufak bir kontrol ile resim yükleme işlemini de çözeceğiz.

student = form.save()
    if 'profile_pic' in request.FILES:
        student.profile_pic = request.FILES['profile_pic']
        student.save()
buradaki profile_pic models'ın içerisinde oluşturduğumuz alanın adı.

eğer request.FILES içerisinde 'profile_pic' var ise bu resmi al ve profile_pic özelliği olarak koy ve formu kaydet.
kaydettikten sonra media isimli yeni bir klasör oluşacak ve içerisine seçtiğimiz profil fotoğrafını kaydedecek.

<!-- 
def student_page(request):
    form = StudentForm(request.POST or None)

    if form.is_valid():
        student = form.save()
        if 'profile_pic' in request.FILES:
            student.profile_pic = request.FILES['profile_pic']
            # ya da 
            # student.profile_pic = request.FILES.get('profile_pic')
            student.save()
        return redirect('index')
        # print(form.cleaned_data.get('first_name'))
    context = {
        'form' : form
    }
    return render(request, 'student/student.html',context)
 -->

çok daha bir pratik yol ise:

def student_form(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        # formu yeniden oluşturup POST verileri ve Dosyaları ekliyoruz.
        if form.is_valid():
            form.save()
            return redirect('/student/')

    context = {
        'form': form
    }
    return render(request, 'student/student.html', context)

------------ BOOTSTRAP ---------------

bootstrapin sitesinden css kısmını aldık ve base.html dosyamızın head kısmına yapıştırdık. js kısmını da body'nin en altına yapıştırdık.

- base.html
div'imize biraz şekil verip bir class ismi verelim. daha sonra student klasörümüzün içinde static/student klasörü oluşturuo içerisine style.css dosyası oluşturalım. bunlar bizim kendi yazacağımız css dosyalarını barındıracak. h3 tagine bir background color verdikten sonra yine base.html dosyasına bu oluşturduğumuz style.css dosyasını bağlayalım:
<link rel="stylesheet" href="{% static 'student/style.css' %}">

<!-- <div style='margin-top: 100px; margin-bottom: 100px' class='container'> -->

djangonun bootstrap ile oluşturulmuş, formları daha güzel görüntülemesi için kullandığı bir tool yükleyeceğiz:
pip install django-crispy-forms
daha sonra bunu settings.py dosyasında installed apps'e kaydedeceğiz:
#3rd part apps
'crispy_forms',
yine settings.py dosyasının en altına şunu ekliyoruz:
CRISPY_TEMPLATE_PACK = 'bootstrap4'

formumuzun olduğu student.html dosyasında da ufak bir ekleme yapacağız:
formun bir üst satırına
{% load crispy_forms_tags %}
ayrıca {{form.as_p}} satırını {{ form | crispy}} olarak değiştireceğiz.

yeni bir eklenti yüklediğimiz için requirements.txt dosyasını yenileyeceğiz.

https://django-crispy-forms.readthedocs.io/en/latest/install.html


django - messages kütüphanesi:

views.py dosyasına messages'i import ediyoruz ve student_page için hazırladığımız view'in içine bir success mesajımızı return redirect'den önce veriyoruz.

<!-- 
from django.contrib import messages

def student_page(request):
    form = StudentForm(request.POST or None)

    if form.is_valid():
        student = form.save()
        if 'profile_pic' in request.FILES:
            student.profile_pic = request.FILES['profile_pic']
            student.save()
        messages.success(request,'Student saved succesfully')
        return redirect('index')
        # print(form.cleaned_data.get('first_name'))
    context = {
        'form' : form
    }
    return render(request, 'student/student.html',context) 
    -->
tabi bu mesajı bir if döngüsü ile base.html sayfasında göstermemiz gerekiyor. biraz bootstrap ile süsleyip bu alerti containerdan önce gösterelim

        {% if messages %}
            {% for message in messages %}
                <div class='alert alert-success'> {{message}} </div>
            {% endfor %}
        {% endif %}


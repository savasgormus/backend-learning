from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

def home_view(request):    
    return render(request, "user_example/home.html")

@login_required
def special(request):  
    return render(request, "user_example/special.html")

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
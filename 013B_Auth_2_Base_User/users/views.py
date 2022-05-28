from multiprocessing import context
from django.shortcuts import render, redirect, HttpResponse

from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from .forms import UserForm, UserProfileForm # forms.py'da oluşturduğumuz formları import ettik.
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def home(request):
    return render(request, 'users/home.html')

def user_logout(request):
    messages.success(request, 'You logged out!')
    logout(request)
    return redirect('home')

def register(request):
    form_user = UserForm()
    form_profile = UserProfileForm()
# 2 tane boş form oluşturduk.

    if request.method == 'POST':
        form_user = UserForm(request.POST)
        form_profile = UserProfileForm(request.POST, request.FILES)
# formları doldurduğumuzda oluşacak durum

        if form_user.is_valid() and form_profile.is_valid():
            user = form_user.save()
            profile = form_profile.save(commit=False)
            profile.user =  user
            profile.save()
            
            login(request, user)
            messages.success(request, 'Register successful')
            return redirect('home')

    context = {
        'form_user': form_user,
        'form_profile': form_profile
    }
# boş formları context'e atadık
    
    return render(request, 'users/register.html', context)
#contexti de template'ime yönlerdirdim
# şimdi bunu urls.py'a göndereceğiz.


def user_login(request):
    form = AuthenticationForm(request, data=request.POST)
    
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('home')
    
    return render(request, 'users/user_login.html', {'form':form})
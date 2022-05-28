from django.shortcuts import render, redirect, HttpResponse

from django.contrib import messages
from django.contrib.auth import logout, login, authenticate

# Create your views here.

def home(request):
    return render(request, 'users/home.html')

def user_logout(request):
    messages.success(request, 'You logged out!')
    logout(request)
    return redirect('home')
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("<h1>Hello world</h1>")

def page2(request):
    return HttpResponse("this is page 2")
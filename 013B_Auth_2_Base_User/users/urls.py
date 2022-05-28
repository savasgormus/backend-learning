from unicodedata import name
from django.urls import path

from users.views import user_logout,register,user_login

urlpatterns = [
    path('logout/',user_logout, name='logout'),
    path('register/', register, name='register'),
# path'imizi girdikten sonra navbar.html dosyasına gidip URL adresini gireceğiz
# href="{% url 'register' %}"
# yine register.html'e gidip form_profile'ı template'imize ekleyeceğiz.
    path('login/',user_login,name='user_login'),
]
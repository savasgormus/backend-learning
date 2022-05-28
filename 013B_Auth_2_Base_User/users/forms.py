from django.contrib.auth.models import User
from .models import UserProfile

from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email')

class UserProfileForm(forms.ModelForm):
# model.py içerisinde ürettiğimiz form'u kullan ve 'user' ı exclude et. tupple şeklinde yaptığımız için
# ('user',) şeklinde bıraktık.
    class Meta:
        model = UserProfile
        exclude = ('user',)


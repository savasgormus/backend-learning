from django import forms
from django.forms import fields
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        models = Student
        fields = '__all__'
from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        models = Student
        fields = '__all__'
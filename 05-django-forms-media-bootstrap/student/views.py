from django.shortcuts import render
from .forms import StudentForm

# Create your views here.

def index(request):
    return render(request, 'student/index.html')

def student_page(request):
    form = StudentForm(request.POST or None)

    if form.is_valid():
        form.save()
        # print(form.cleaned_data.get('first_name'))
    context = {
        'form' : form
    }
    return render(request, 'student/student.html',context)
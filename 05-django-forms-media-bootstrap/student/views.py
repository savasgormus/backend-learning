from django.shortcuts import render
from .forms import StudentForm

# Create your views here.

def index(request):
    return render(request, 'student/index.html')

def student_page(request):
    # formStudent = StudentForm()
    context = {
        'form' : StudentForm()
    }
    return render(request, 'student/student.html',context)
from django.shortcuts import render, redirect
from .forms import StudentForm
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'student/index.html')

def student_page(request):
    form = StudentForm(request.POST or None)

    if form.is_valid():
        student = form.save()
        if 'profile_pic' in request.FILES:
            student.profile_pic = request.FILES['profile_pic']
            student.save()
        messages.success(request,'Student saved succesfully')
        # messages.error(request,' testing failed')
        return redirect('index')
        # print(form.cleaned_data.get('first_name'))
    context = {
        'form' : form
    }
    return render(request, 'student/student.html',context)
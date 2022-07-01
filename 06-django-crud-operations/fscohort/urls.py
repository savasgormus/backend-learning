from django.urls import path
from .views import index, student_add, student_list

urlpatterns = [
    path('', index, name='home'),
    path('list/', student_list,name='list'),
    path('add/', student_add, name='add')
]

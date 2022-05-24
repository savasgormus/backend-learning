from django.urls import path
from .views import home, page2

urlpatterns = [
    path('', home, name='home'),
    path('page2/', page2, name="page2")
]

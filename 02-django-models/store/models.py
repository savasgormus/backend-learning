from django.db import models

# Create your models here.

class Category(models.Model) :
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)

class Product(models.Model) :
    name = models.CharField(max_length=20)
    number = models.CharField(max_length=20)
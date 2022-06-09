from contextlib import nullcontext
from django.db import models

# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name =  models.CharField(max_length=50)
    number = models.IntegerField()
    about = models.TextField(null=True, blank=True)
    avatar = models.ImageField(null=True, blank=True, upload_to='media/')

    def __str__(self):
        return (f"{self.first_name} {self.last_name}")

    class Meta:
        ordering = ["number"]
        verbose_name_plural = "Öğrenciler"  
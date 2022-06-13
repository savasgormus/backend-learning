from contextlib import nullcontext
from email.policy import default
from django.db import models

# Create your models here.


class Student(models.Model):

    YEAR_IN_SCHOOL_CHOICES = [
        ("FR", 'Freshman'),
        ("SP", 'Sophomore'),
        ("JR", 'Junior'),
        ("SR", 'Senion'),
        ("GRD", 'Graduate'),
    ]

    first_name = models.CharField(max_length=50)
    last_name =  models.CharField(max_length=50)
    number = models.IntegerField()
    about = models.TextField(null=True, blank=True)
    avatar = models.ImageField(null=True, blank=True, upload_to='media/')
    register_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True )
    year_in_school = models.CharField(max_length=3, choices=YEAR_IN_SCHOOL_CHOICES)

    def __str__(self):
        return (f"{self.first_name} {self.last_name}")

    class Meta:
        ordering = ["number"]
        verbose_name_plural = "Öğrenciler"  
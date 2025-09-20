from django.db import models

# Create your models here.
class Student(models.Model):
    stud_name=models.CharField( max_length=50)
    age=models.IntegerField()
    place=models.CharField(max_length=50)
    email=models.EmailField()
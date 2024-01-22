from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    usertype = models.CharField(max_length=20)

class department(models.Model):
    dept_name = models.CharField(max_length=20)

class student(models.Model):
    stud_id =models.ForeignKey(User, on_delete=models.CASCADE)
    dept_id =models.ForeignKey(department, on_delete=models.CASCADE)
    address = models.CharField(max_length=20)
    phone = models.IntegerField()
   

class teacher(models.Model):
    teacher_id =models.ForeignKey(User, on_delete=models.CASCADE)
    dept_id =models.ForeignKey(department, on_delete=models.CASCADE)
    address = models.CharField(max_length=20)
    phone = models.IntegerField()
    salary = models.IntegerField()
    experience = models.IntegerField()


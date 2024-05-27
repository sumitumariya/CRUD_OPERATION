from django.db import models

# Create your models here.
class Student(models.Model):
    Name =models.CharField(max_length=50)
    Email=models.EmailField()
    Contact=models.CharField(max_length=10)
    Password=models.CharField(max_length=10)

class Query(models.Model):
    Email=models.EmailField()
    Title=models.CharField(max_length=100)
    discription=models.CharField(max_length=100)
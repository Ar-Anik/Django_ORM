from django.db import models

# Create your models here.

class Teacher(models.Model):
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    classroom = models.IntegerField()
    teacher = models.CharField(max_length=50)

    def __str__(self):
        return self.name

from django.db import models

# Create your models here.

class Teacher(models.Model):
    name = models.CharField(max_length=25)
    subject = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Student(models.Model):
    firstname = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)
    age = models.IntegerField()
    classroom = models.IntegerField()
    teacher = models.CharField(max_length=25)

    def __str__(self):
        return self.surname
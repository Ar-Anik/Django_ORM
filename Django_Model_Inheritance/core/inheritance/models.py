from django.db import models

# Create your models here.

######################   Abstract Model    ####################

class Baseclass(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
        ordering = ['name']

class Student(Baseclass):
    classroom = models.IntegerField()
    semester = models.CharField(max_length=20)

    class Meta(Baseclass.Meta):
        ordering = ['-created']


class Teacher(Baseclass):
    subject = models.CharField(max_length=20)


####################### Multi-Table Model Inheritance #######################


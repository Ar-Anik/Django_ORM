from django.db import models

# Create your models here.

class Course(models.Model):
    Credits = (
        ('1', '0.75'),
        ('2', '1'),
        ('3', '2'),
        ('4', '3'),
        ('5', '4'),
        ('6', '5'),
        ('7', '6'),
    )

    course_code = models.CharField(max_length=20, default="CSE-101", unique=True)
    course_name = models.CharField(max_length=50, default="C Language", unique=True)
    course_credit = models.CharField(max_length=1, choices=Credits, default='4')

    def __str__(self):
        return self.course_code


class Student(models.Model):
    std_name = models.CharField(max_length=40)
    std_id = models.CharField(max_length=50, primary_key=True)
    std_email = models.EmailField(max_length=50, unique=True, blank=True)

    course = models.ManyToManyField(Course)

    def __str__(self):
        return self.std_id


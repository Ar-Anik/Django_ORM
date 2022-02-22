from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Bangladeshi(models.Model):
    Name = models.CharField(max_length=100)
    Nid = models.CharField(max_length=100)
    phone = PhoneNumberField(blank=True)

    def __str__(self):
        return self.Nid

class Student(models.Model):
    person = models.OneToOneField("Bangladeshi", on_delete=models.CASCADE)
    school_name = models.CharField(max_length=100)
    std_id = models.IntegerField()

    def __str__(self):
        return str(self.std_id)



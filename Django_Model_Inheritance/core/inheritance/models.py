from django.db import models

# Create your models here.

# docs.djangoproject.com/en/4.0/topics/db/models/#abstract-base-classes
#########################  Abstract Model  ###########################

class Baseclass(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['name']

class Student(Baseclass):
    classroom = models.IntegerField()
    semester = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Teacher(Baseclass):
    subject = models.CharField(max_length=20)

    def __str__(self):
        return self.name


###########################   Abstract Model    #############################

class PersonalInfo(models.Model):
    Married_Status = (
        ("1", "Married"),
        ("2", "Unmarried"),
    )

    Name = models.CharField(max_length=50)
    Age = models.IntegerField()
    Married_Status = models.CharField(max_length=10, choices=Married_Status, default=2)

    Birth_Date = models.DateField(default="Day/Month/Year")

    class Meta:
        abstract = True
        ordering = ['Age']


class FamilyInfo(models.Model):
    Father_Name = models.CharField(max_length=50)
    Mother_Name = models.CharField(max_length=50)
    Number_of_Sibling = models.IntegerField()

    class Meta:
        abstract = True
        ordering = ['Number_of_Sibling']

class OfficeInfo(PersonalInfo, FamilyInfo):
    Status = (
        ("1", "Worker"),
        ("2", "Manager"),
        ("3", "HR Manager"),
        ("4", "CMO"),
        ("5", "CEO"),
    )

    Office_id = models.BigIntegerField(default=1810101, primary_key=True)
    Position_Rank = models.CharField(max_length=10, choices=Status, default=1)

    class Meta(PersonalInfo.Meta, FamilyInfo.Meta):
        pass

    def __str__(self):
        return str(self.Office_id)


# docs.djangoproject.com/en/4.0/topics/db/models/#multi-table-inheritance
####################### Multi-Table Model Inheritance #######################

class Books(models.Model):
    Book_Name = models.CharField(max_length=50)
    Author_Name = models.CharField(max_length=50)
    Price = models.FloatField()

    def __str__(self):
        return self.Book_Name


class ISBN(Books):
    books_ptr = models.OneToOneField(Books, on_delete=models.CASCADE, parent_link=True, primary_key=True)
    Isbn = models.CharField(max_length=50, unique=True, null=True, blank=True)

# https://www.benlopatin.com/using-django-proxy-models/
################################ Proxy Model ##############################

STORY_TYPES = (
    ('f', 'Feature'),
    ('i', 'Infographic'),
)

class Story(models.Model):
    type = models.CharField(max_length=1, choices=STORY_TYPES)
    title = models.CharField(max_length=100)
    body = models.TextField(blank=True, null=True)
    infographic = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title

class FeatureManager(models.Manager):
    def get_queryset(self):
        return super(FeatureManager, self).get_queryset().filter(type='f')

class InfographicManager(models.Manager):
    def get_queryset(self):
        return super(InfographicManager, self).get_queryset().filter(type='i')


class FeatureStory(Story):
    objects = FeatureManager()
    class Meta:
        proxy = True


class InfographicStory(Story):
    objects = InfographicManager()
    class Meta:
        proxy = True

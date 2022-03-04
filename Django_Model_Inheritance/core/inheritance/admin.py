from django.contrib import admin
from .models import FeatureStory, InfographicStory, Story, Student, Teacher, OfficeInfo, Books, ISBN

# Register your models here.

@admin.register(Student)
class PostAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'semester']

@admin.register(Teacher)
class PostAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject']

@admin.register(OfficeInfo)
class PostAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Office_id', 'Position_Rank']

@admin.register(Books)
class PostAdmin(admin.ModelAdmin):
    list_display = ['Book_Name', 'Author_Name', 'Price']

@admin.register(ISBN)
class PostAdmin(admin.ModelAdmin):
    list_display = ['Book_Name', 'Author_Name', 'Isbn']

@admin.register(Story)
class PostAdmin(admin.ModelAdmin):
    list_display = ['type', 'title']

@admin.register(InfographicStory)
class PostAdmin(admin.ModelAdmin):
    list_display = ['type', 'title']

@admin.register(FeatureStory)
class PostAdmin(admin.ModelAdmin):
    list_display = ['type', 'title']
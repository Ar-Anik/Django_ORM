from django.contrib import admin
from .models import Course, Student

# Register your models here.

@admin.register(Course)
class PostAdmin(admin.ModelAdmin):
    list_display = ['course_name', 'course_code', 'course_credit']

@admin.register(Student)
class PostAdmin(admin.ModelAdmin):
    list_display = ['std_name', 'std_id', 'std_email']


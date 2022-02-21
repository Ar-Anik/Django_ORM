from django.shortcuts import render
from .models import Student, Teacher
from django.db import connection
from django.db.models import Q

# Create your views here.

def student_list(request):
    posts = Student.objects.all()
    
    print(posts)
    print(connection.queries)

    context = {
        'data': posts,
    }

    return render(request, 'output.html', context)

def teacher_list(request):
    posts = Teacher.objects.all()

    print(posts)
    print(connection.queries)

    context = {
        'data': posts,
    }

    return render(request, 'output.html', context)


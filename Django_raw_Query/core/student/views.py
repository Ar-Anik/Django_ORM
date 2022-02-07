from django.shortcuts import render
from .models import Student, Teacher
from django.db import connection
from django.db.models import Q

# Create your views here.

def list(request):
    posts = Student.objects.raw("SELECT * FROM student_student")

    print(posts)
    print(connection.queries)

    context = {
        'data': posts,
    }

    return render(request, 'output.html', context)

def where(request):
    posts = Student.objects.raw("SELECT * FROM student_student WHERE age=21")

    context = {
        'data': posts,
    }

    return render(request, 'output.html', context)

def loop(request):
    posts = Student.objects.all()

    for i in Student.objects.raw("SELECT * FROM student_student"):
        print(i)

    context = {
        'data': posts,
    }

    return render(request, 'output.html', context)

def variable(request):
    sql = "SELECT * FROM student_student"
    posts = Student.objects.raw(sql)

    context = {
        'data': posts,
    }

    return render(request, 'output.html', context)

def limiting_query(request):
    sql = "SELECT * FROM student_student"
    posts = Student.objects.raw(sql)[1:4]

    context = {
        'data': posts,
    }

    return render(request, 'output.html', context)



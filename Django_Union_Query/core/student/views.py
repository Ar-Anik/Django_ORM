from django.shortcuts import render
from .models import Student, Teacher
from django.db import connection
from django.db.models import Q

# Create your views here.

def list(request):
    posts = Student.objects.all().values_list('name').union(Teacher.objects.all().values_list('name'))

    print(posts)
    print(connection.queries)

    context = {
        'posts': posts,
    }

    return render(request, 'output.html', context)

def allvalue(request):
    posts = Student.objects.all().values_list('id', 'name').union(Teacher.objects.all().values_list('id', 'name'))

    print(posts)
    print(connection.queries)

    context = {
        'posts': posts,
    }

    return render(request, 'output.html', context)

def values(request):
    posts = Student.objects.values('name').union(Teacher.objects.values('name'))

    print(posts)
    print(connection.queries)

    context = {
        'posts': posts,
    }

    return render(request, 'output.html', context)

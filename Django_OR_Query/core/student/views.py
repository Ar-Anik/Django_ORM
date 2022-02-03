from django.shortcuts import render
from .models import Student
from django.db import connection
from django.db.models import Q

# Create your views here.

def student_list(request):
    posts = Student.objects.all()

    print(posts)
    print(posts.query)
    print(connection.queries)

    context = {
        'posts': posts,
    }

    return render(request, 'output.html', context)

def or_query(request):
    posts = Student.objects.filter(surname__startswith='anik')|Student.objects.filter(surname__startswith='anis')

    print(posts)
    print(connection.queries)

    context = {
        'posts': posts,
    }

    return render(request, 'output.html', context)

def Q_object(request):
    posts = Student.objects.filter(Q(surname__startswith='anik') | Q(surname__startswith='anis'))

    print(posts)
    print(connection.queries)

    context = {
        'posts': posts,
    }

    return render(request, 'output.html', context)

def Not_Q_object(request):
    posts = Student.objects.filter(~Q(surname__startswith='anik'))

    print(posts)
    print(connection.queries)

    context = {
        'posts': posts,
    }

    return render(request, 'output.html', context)

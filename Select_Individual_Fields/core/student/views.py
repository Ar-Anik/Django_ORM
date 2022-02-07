from django.shortcuts import render
from .models import Student, Teacher
from django.db import connection
from django.db.models import Q

# Create your views here.

def list(request):
    posts = Student.objects.filter(classroom=102).only('name')

    print(posts)
    print(connection.queries)

    context = {
        'data': posts,
    }

    return render(request, 'output.html', context)

def selector(request):
    posts = Student.objects.filter(Q(classroom=101) | Q(classroom=103)).only('name', 'age')

    print(posts)
    print(connection.queries)

    context = {
        'data': posts,
    }

    return render(request, 'output1.html', context)

def onefield(request):
    posts = Student.objects.only('name')

    print(posts)
    print(connection.queries)

    context = {
        'data': posts,
    }

    return render(request, 'output2.html', context)

def manyfield(request):
    posts = Student.objects.only('name', 'age')

    print(posts)
    print(connection.queries)

    context = {
        'data': posts,
    }

    return render(request, 'output1.html', context)

def cancel(request):
    posts = Student.objects.defer('name')

    print(posts)
    print(connection.queries)

    context = {
        'data': posts,
    }

    return render(request, 'output3.html', context)

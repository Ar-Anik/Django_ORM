from django.shortcuts import render
from .models import Student
from django.db import connection
from django.db.models import Q

# Create your views here.

def list(request):
    posts = Student.objects.filter(classroom=101) & Student.objects.filter(surname__startswith='anik')

    print(posts)
    print(connection.queries)

    context = {
        'posts': posts,
    }

    return render(request, 'output.html', context)

def qand(request):
    posts = Student.objects.filter(Q(classroom=101) & Q(surname__startswith='anik'))

    print(posts)
    print(connection.queries)

    context = {
        'posts': posts,
    }

    return render(request, 'output.html', context)

from django.shortcuts import render
from .models import Student
from django.db import connection
from django.db.models import Q

# Create your views here.

def list(request):
    posts = Student.objects.exclude(age=20)

    print(posts)
    print(connection.queries)

    context = {
        'posts': posts,
    }

    return render(request, 'output.html', context)

# gt = Greater than ----------> Entry.objects.filter(id__gt=4)
# gte = Greater than or equal to 
# lt = Less than
# lte = Less than or equal to

def list_gte(request):
    posts = Student.objects.exclude(age__gte=21)

    print(posts)
    print(connection.queries)

    context = {
        'posts': posts,
    }

    return render(request, 'output.html', context)

def list_lte(request):
    posts = Student.objects.exclude(age__lte=21)

    print(posts)
    print(connection.queries)

    context = {
        'posts': posts,
    }

    return render(request, 'output.html', context)

def qnot(request):
    posts = Student.objects.filter(~Q(age__lt=21)) & Student.objects.filter(~Q(name__startswith='fahim'))

    print(posts)
    print(connection.queries)

    context = {
        'posts': posts,
    }

    return render(request, 'output.html', context)

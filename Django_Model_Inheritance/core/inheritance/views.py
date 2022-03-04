from django.db import connection
from django.shortcuts import render
from .models import Books, ISBN, Student, Teacher, OfficeInfo

# Create your views here.

def Std_List(request):
    data = Student.objects.all()

    print(data)
    print(connection.queries)

    context = {
        'data' : data,
    }

    return render(request, 'output.html', context)

def Thr_List(request):
    data = Teacher.objects.all()

    print(data)
    print(connection.queries)

    context = {
        'data':data,
    }

    return render(request, 'output.html', context)

def Employer_List(request):
    data = OfficeInfo.objects.all()

    print(data)
    print(connection.queries)

    context = {
        'data': data,
    }

    return render(request, 'output.html', context)


def Book_List(request):
    data = Books.objects.all()

    print(data)
    print(connection.queries)

    context = {
        'data':data,
    }

    return render(request, 'output.html', context)

def Book_ISBN(request):
    data = ISBN.objects.all()

    print(data)
    print(connection.queries)

    context = {
        'data' : data,
    }

    return render(request, 'output.html', context)

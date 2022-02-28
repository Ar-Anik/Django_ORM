from django.shortcuts import render
from .models import Student

# Create your views here.

def student_list(request):
    data = Student.objects.all()

    context = {
        'data' : data,
    }

    return render(request, 'studentlist.html', context)

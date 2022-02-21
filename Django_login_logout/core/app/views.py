from django.shortcuts import redirect, render
from .models import Student
from .forms import Rform, Istudent
from django.contrib.auth.decorators import login_required

# Create your views here.

def registrationform(request):
    reg = Rform()
    string = "Enter Information"

    if request.method == "POST":
        reg = Rform(request.POST)
        string = "Something is Wrong"

        if reg.is_valid():
            reg.save()
            return redirect('/login')

    context = {
        'form': reg,
        'string': string,
    }

    return render(request, 'registration.html', context)


def studentlist(request):
    data = Student.objects.all()

    context = {
        'data': data,
    }

    return render(request, 'studentlist.html', context)

@login_required(login_url='/login')
def studentform(request):
    reg = Istudent()
    string = "Please Inter Currect Information"

    if request.method == "POST":
        reg = Istudent(request.POST)
        string = "Not Currect Information"

        if reg.is_valid():
            reg.save()
            return redirect('/studentlist')

    context = {
        'form': reg,
        'string': string,
    }

    return render(request, 'student.html', context)

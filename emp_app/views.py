from django.shortcuts import render
from .models import Department, Role, Employee
# Create your views here.


def index(request):
    return render(request, 'index.html')


def add(request):
    return render(request, 'add_emp.html')


def view(request):
    emp = Employee.objects.all()
    context = {"emps": emp, }
    print(context)
    return render(request, 'view_all.html', context=context)


def remove(request):
    return render(request, 'remove_emp.html')


def filter(request):
    return render(request, 'filter_emp.html')

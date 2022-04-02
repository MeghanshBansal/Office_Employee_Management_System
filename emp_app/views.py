from django.shortcuts import render, HttpResponse
import datetime
from .models import *
# Create your views here.


def index(request):
    return render(request, 'index.html')


def add(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dept = int(request.POST['dept'])
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        role = int(request.POST['role'])
        phone = int(request.POST['phone'])
        new_emp = Employee(first_name=first_name, last_name=last_name, dept_id=dept, salary=salary,
                           bonus=bonus, role_id=role, phone=phone, hire_date=datetime.date.today())
        new_emp.save()
        return HttpResponse("Employee Created")
    elif request.method == 'GET':
        depts = Department.objects.all()
        roles = Role.objects.all()
        c = {"depts": depts, "roles": roles, }
        return render(request, 'add_emp.html', context=c)
    else:
        return HttpResponse("Error Occured")


def view(request):
    emp = Employee.objects.all()
    context = {"emps": emp, }
    return render(request, 'view_all.html', context=context)


def remove(request):
    return render(request, 'remove_emp.html')


def filter(request):
    return render(request, 'filter_emp.html')

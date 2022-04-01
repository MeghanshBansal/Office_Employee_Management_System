from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def add(request):
    return render(request, 'add_emp.html')


def view(request):
    return render(request, 'view_all.html')


def remove(request):
    return render(request, 'remove_emp.html')


def filter(request):
    return render(request, 'filter_emp.html')

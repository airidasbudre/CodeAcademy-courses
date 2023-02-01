from django.shortcuts import render
from django.http import HttpResponse
from .models import Client, Employee, Project, Work, Invoice


def index(request):
    num_projects = Project.objects.all().count()
    num_works = Work.objects.all().count()
    num_clients = Client.objects.count()
    num_employees = Employee.objects.all().count()

    context = {
        'num_projects': num_projects,
        'num_works': num_works,
        'num_clients': num_clients,
        'num_employees': num_employees,
    }

    # renderiname index.html, su duomenimis kintamąjame context
    return render(request, 'index.html', context=context)

def home(request):
    return render(request, 'base.html')

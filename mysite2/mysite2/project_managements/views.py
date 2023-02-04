from django.shortcuts import render
from django.http import HttpResponse
from .models import Client, Employee, Project, Work, Invoice
from django.views import generic
from django.views import View
from django.views.generic import TemplateView



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

class HomePageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'base.html')

# class ProjectsView(View):
#     def get(self, request, *args, **kwargs):
#         projects = Project.objects.all()
#         return render(request, 'projects.html', {'projects': projects})

class ProjectsView(TemplateView):
    template_name = 'projects.html'
    context_object_name = 'projects'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        return context

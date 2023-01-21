from django.shortcuts import render
from django.http import HttpResponse
from .models import Car_model, Service, Order, Cars, Orderline, Employees
from django.views import generic


def index(request):
    num_car_model = Car_model.objects.count()
    num_service = Service.objects.count()
    num_emplyees = Employees.objects.count()

    context = {
        "num_car_model" : num_car_model,
        "num_service" : num_service, 
        "num_employees" : num_emplyees

    }
    return render(request, 'index.html', context=context)

def cars(request):
    
    cars = Cars.objects.all()
    context = {
        'cars': cars
    }
    print(cars)
    return render(request, 'cars.html', context=context)

class ServiceListView(generic.ListView):
    model = Service
    template_name = 'service.html'
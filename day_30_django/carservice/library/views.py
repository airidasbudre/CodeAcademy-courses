from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Car_model, Service, Order, Cars, Orderline, Employees
from django.views import generic



def index(request):
    num_car_model = Car_model.objects.count()
    num_service = Service.objects.count()
    num_emplyees = Employees.objects.count()
    
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1
    context = {
        "num_car_model" : num_car_model,
        "num_service" : num_service, 
        "num_employees" : num_emplyees,
        'num_visits': num_visits,

    }
    return render(request, 'index.html', context=context)

def cars(request):
    
    cars = Cars.objects.all()
    context = {
        'cars': cars,
    }
    return render(request, 'cars.html', context=context)

class ServiceListView(generic.ListView):
    model = Service
    template_name = 'service.html'
    context_object_name = "service"

def car(request, car_id):
    car = get_object_or_404(Cars, pk=car_id)
    context = {
        'car': car,
    }
    return render(request, 'car.html', context=context)

class EmployeesListView(generic.ListView):
    model = Employees
    template_name = 'employees.html'
    context_object_name = "employees"
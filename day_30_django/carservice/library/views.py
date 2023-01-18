from django.shortcuts import render
from django.http import HttpResponse
from .models import Car_model, Service, Order, Cars, Orderline


def index(request):
    num_car_model = Car_model.objects.all().count()
    num_service = Service.objects.all().count()

    context = {
        "num_car_model" : num_car_model,
        "num_service" : num_service, 
    }

    return render(request, 'index.html', context=context)
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Car_model, Service, Order, Cars, Orderline, Employees
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required



def index(request):
    num_car_model = Car_model.objects.count()
    num_service = Service.objects.count()
    num_cars_amount = Cars.objects.count()
    num_order_amount = Order.objects.filter(status__exact='i').count()
    num_emplyees = Employees.objects.count()
    
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1
    context = {
        "num_car_model" : num_car_model,
        "num_service" : num_service, 
        "num_cars_amount": num_cars_amount,
        "num_order_amount": num_order_amount,
        "num_employees" : num_emplyees,
        'num_visits': num_visits,

    }
    return render(request, 'index.html', context=context)

def cars(request):
    paginator = Paginator(Cars.objects.all(), 3)
    page_number = request.GET.get('page')
    paged_cars = paginator.get_page(page_number)
    cars = Cars.objects.all()
    context = {
        'cars': paged_cars,
    }
    return render(request, 'cars.html', context=context)

class OrderListView(generic.ListView):
    model = Order
    paginate_by = 3
    template_name = 'orders.html'
    context_object_name = "orders"

class OrderDetailView(generic.DetailView):
    model = Order
    template_name = "order.html"
    context_object_name = "order"

def search(request):
    query = request.GET.get('query')
    search_results = Cars.objects.filter(
        Q(client__icontains=query) | Q(car_model__brand__icontains=query) | Q(car_model__model__icontains=query) | Q(license_plate__icontains=query) | Q(
            vin_code__icontains=query))
    return render(request, 'search.html', {'cars': search_results, 'query': query})

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


class UserOrderListView(generic.ListView):
    model = Order
    paginate_by = 3
    template_name = "user_order.html"
    context_object_name = "orders"
    
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
    
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    return render(request, 'profile.html')
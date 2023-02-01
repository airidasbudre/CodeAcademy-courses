from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from .models import Car_model, Service, Order, Cars, Orderline, Employees, Profile
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.forms import User
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormMixin
from .forms import OrderCreateUpdateForm, OrderCommentForm, UserUpdateForm, ProfileUpdateForm, OrderCreateUpdateForm
from django.contrib import messages




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
    context = {
        'cars': paged_cars,
    }
    return render(request, 'cars.html', context=context)

def car(request, car_id):
    car = get_object_or_404(Cars, pk=car_id)
    context = {
        'car': car,
    }
    return render(request, 'car.html', context=context)

def search(request):
    query = request.GET.get('query')
    search_results = Cars.objects.filter(
        Q(client__icontains=query) | Q(car_model__brand__icontains=query) | Q(car_model__model__icontains=query) | Q(license_plate__icontains=query) | Q(
            vin_code__icontains=query))
    return render(request, 'search.html', {'cars': search_results, 'query': query})

@csrf_protect
def register(request):
    if request.method == "POST":
        # pasiimame reikšmes iš registracijos formos
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # tikriname, ar sutampa slaptažodžiai
        if password == password2:
            # tikriname, ar neužimtas username
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Vartotojo vardas {username} užimtas!')
                return redirect('register')
            else:
                # tikriname, ar nėra tokio pat email
                if User.objects.filter(email=email).exists():
                    messages.error(request, f'user su el. paštu {email} jau užregistruotas!')
                    return redirect('register')
                else:
                    # jeigu viskas tvarkoje, sukuriame naują vartotoją
                    User.objects.create_user(username=username, email=email, password=password)
                    messages.info(request, f'user {username} užregistruotas!')
                    return redirect('login')
        else:
            messages.error(request, 'Slaptažodžiai nesutampa!')
            return redirect('register')
    return render(request, 'register.html')

@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Profilis atnaujintas")
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'profile.html', context)

class OrderListView(generic.ListView):
    model = Order
    paginate_by = 3
    template_name = 'orders.html'
    context_object_name = "orders"

class UserOrderListView(generic.ListView):
    model = Order
    paginate_by = 3
    template_name = "user_order.html"
    context_object_name = "orders"
    
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

class OrderDetailView(generic.DetailView):
    model = Order
    template_name = "order.html"
    context_object_name = "order"

    def get_success_url(self):
        return reverse('order', kwargs={'pk': self.object.id})

    # standartinis post metodo perrašymas, naudojant FormMixin, galite kopijuoti tiesiai į savo projektą.
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.order = self.object
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)
    
class OrderCreateView(LoginRequiredMixin, generic.CreateView):
    model = Order
    # fields = ['terminas', 'automobilis', 'status']
    success_url = "/autoservice/myorders/"
    template_name = "order_form.html"
    form_class = OrderCreateUpdateForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EmployeesListView(generic.ListView):
    model = Employees
    template_name = 'employees.html'
    context_object_name = "employees"

class UserOrderUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Order
    # fields = ['terminas', 'automobilis', 'status']
    # success_url = "/autoservice/manouzsakymai/"
    template_name = "order_form.html"
    form_class = OrderCreateUpdateForm

    def get_success_url(self):
        return reverse("order", kwargs={"pk": self.object.id})

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        order = self.get_object()
        return self.request.user == order.user
    
class UserUsakymasDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Order
    success_url = "/autoservice/manouzsakymai/"
    template_name = "user_order_delete.html"
    context_object_name = "order"

    def test_func(self):
        order = self.get_object()
        return self.request.user == order.user



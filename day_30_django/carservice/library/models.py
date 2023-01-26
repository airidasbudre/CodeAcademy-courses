from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date


class Service(models.Model):
    name = models.CharField('Name', max_length=200, help_text='Įveskite paslaugos pavadinimą')
    price = models.FloatField('Price')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'


class Car_model(models.Model):
    brand = models.CharField('Brand_name', max_length=200, help_text='Brand name')
    model = models.CharField('Model', max_length=200, help_text='Model name')
    due_back = models.DateField('Year of made', null=True, blank=True)

    def __str__(self):
        return f"{self.brand} {self.model}"

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('car-detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Car model'
        verbose_name_plural = 'Car models'

class Cars(models.Model):
    license_plate = models.CharField('License_plate', max_length=200)
    car_model = models.ForeignKey('Car_model', on_delete=models.SET_NULL, null=True)
    client = models.CharField('Client', max_length=200)
    vin_code = models.CharField('Vin_code', max_length=200)

    def __str__(self):
        return f'{self.license_plate} {self.car_model} {self.client}'

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('cars', args=[str(self.id)])

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'

class Order(models.Model):
    date = models.DateTimeField(verbose_name="Date", auto_now_add=True)
    cars = models.ForeignKey('Cars', on_delete=models.SET_NULL, null=True)
    amount = models.CharField('Amount', max_length=200)
    reader = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False


    LOAN_STATUS = (
        ('a', 'Administruojama'),
        ('p', 'Paimta'),
        ('g', 'Galima paimti'),
        ('r', 'Rezervuota'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='p',
        help_text='Statusas',)

    def amount(self):
        amount = 0
        lines = self.lines.all()
        for line in lines:
            amount += line.price()
        return amount

    def __str__(self):
        return f'{self.cars} ({self.date})'

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

class Orderline(models.Model):
    service = models.ForeignKey('Service', on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey('Order', on_delete=models.CASCADE, null=True, related_name="lines")
    quantity = models.IntegerField('Quantity')
    
    
    def price(self):
        return self.service.price * self.quantity

    def __str__(self):
        return f'{self.order.date}, {self.service} ({self.quantity})'

    class Meta:
        verbose_name = 'Orderline'
        verbose_name_plural = 'Orderlines'

class Employees(models.Model):
    e_name = models.CharField('E_name', max_length=200)
    e_surname = models.CharField('E_surname', max_length=200)
    position = models.CharField('Position', max_length=200)

    def __str__(self):
        return f'{self.e_name}, {self.e_surname}, {self.position}'


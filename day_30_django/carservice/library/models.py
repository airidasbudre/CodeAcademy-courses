from django.db import models
from django.urls import reverse


class Service(models.Model):
    name = models.CharField('Name', max_length=200, help_text='Įveskite paslaugos pavadinimą')
    price = models.IntegerField('Price')

    def __str__(self):
        return self.name

    def __str__(self):
        return self.price


class Car_model(models.Model):
    brand = models.CharField('Brand_name', max_length=200, help_text='Brand name')
    model = models.CharField('Model', max_length=200, help_text='Model name')
    due_back = models.DateField('Year of made', null=True, blank=True)

    def __str__(self):
        return self.brand

    def __str__(self):
        return self.model

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('car-detail', args=[str(self.id)])

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

class Order(models.Model):
    date = models.DateField('Order_date', null=True, blank=True)
    cars = models.ForeignKey('Cars', on_delete=models.SET_NULL, null=True)
    amount = models.CharField('Amount', max_length=200)

    def __str__(self):
        return f'{self.date} {self.cars} {self.amount}'

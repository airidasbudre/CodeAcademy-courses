from django.contrib import admin
from .models import Car_model, Service, Order, Cars, Orderline


class OrderAdmin(admin.ModelAdmin):
    list_display = ('date', 'cars', 'amount')
    search_fields = ('cars', 'date')

class CarsAdmin(admin.ModelAdmin):
    list_display = ('license_plate', 'car_model', 'client', 'vin_code')
    list_filter = ('car_model', 'client')
    search_fields = ('license_plate', 'client')

# class OrderAdmin(admin.ModelAdmin):
#     list_display = ('date', 'cars', 'amount')
#     search_fields = ('cars', 'date') 

admin.site.register(Car_model)
admin.site.register(Service)
admin.site.register(Order, OrderAdmin)
admin.site.register(Cars, CarsAdmin)
admin.site.register(Orderline)

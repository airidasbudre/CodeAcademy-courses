from django.contrib import admin
from .models import Car_model, Service, Order, Cars, Orderline, Employees


class OrderAdmin(admin.ModelAdmin):
    list_display = ('date', 'cars', 'amount', 'reader')
    search_fields = ('cars', 'date', 'reader')

    fieldsets = (
        (None, {
            'fields': ('cars', 'date')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'reader')
        }),
    )
    

class CarsAdmin(admin.ModelAdmin):
    list_display = ('license_plate', 'car_model', 'client', 'vin_code')
    list_filter = ('car_model', 'client')
    search_fields = ('license_plate', 'client')

class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('e_name', 'e_surname', 'position')

# class OrderAdmin(admin.ModelAdmin):
#     list_display = ('date', 'cars', 'amount')
#     search_fields = ('cars', 'date') 

admin.site.register(Car_model)
admin.site.register(Service)
admin.site.register(Order, OrderAdmin)
admin.site.register(Cars, CarsAdmin)
admin.site.register(Orderline)
admin.site.register(Employees, EmployeesAdmin)
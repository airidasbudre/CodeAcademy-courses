from django.contrib import admin
from .models import Car_model, Service, Order, Cars, Orderline, Employees, Profile


class OrderlineInLine(admin.TabularInline):
    model = Orderline
    extra = 0

class OrderlineAdmin(admin.ModelAdmin):
    list_display = ('order', 'service', 'quantity', 'price')
    

class OrderAdmin(admin.ModelAdmin):
    list_display = ('date', 'cars', 'amount', 'duration', 'user')
    inlines = [OrderlineInLine]

    # fieldsets = (
    #     (None, {
    #         'fields': ('cars', 'date')
    #     }),
    #     ('Availability', {
    #         'fields': ('status', 'due_back', 'reader')
    #     }),
    # )
    

class CarsAdmin(admin.ModelAdmin):
    list_display = ('license_plate', 'car_model', 'client', 'vin_code')
    list_filter = ('car_model', 'client')
    search_fields = ('license_plate', 'client')

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('e_name', 'e_surname', 'position')

# class OrderAdmin(admin.ModelAdmin):
#     list_display = ('date', 'cars', 'amount')
#     search_fields = ('cars', 'date') 

admin.site.register(Car_model)
admin.site.register(Order, OrderAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Cars, CarsAdmin)
admin.site.register(Orderline, OrderlineAdmin)
admin.site.register(Employees, EmployeesAdmin)
admin.site.register(Profile)
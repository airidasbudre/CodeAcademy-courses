from django.contrib import admin
from .models import Car_model, Service, Order, Cars


admin.site.register(Car_model)
admin.site.register(Service)
admin.site.register(Order)
admin.site.register(Cars)
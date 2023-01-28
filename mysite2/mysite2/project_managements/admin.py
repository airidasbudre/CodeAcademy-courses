from django.contrib import admin
from .models import Project, Client, Employee, Work, Invoice

# Register your models here.
admin.site.register(Project)
admin.site.register(Client)
admin.site.register(Employee)
admin.site.register(Work)
admin.site.register(Invoice)

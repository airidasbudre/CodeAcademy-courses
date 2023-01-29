from django.contrib import admin
from .models import Project, Client, Employee, Work, Invoice, ClientAdmin
from import_export.admin import ImportExportModelAdmin


# Register your models here.
admin.site.register(Project)
admin.site.register(Client, ClientAdmin)
admin.site.register(Employee)
admin.site.register(Work)
admin.site.register(Invoice)


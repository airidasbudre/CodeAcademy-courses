from django.contrib import admin
from .models import Project, Client, Employee, Work, Invoice, ClientAdmin
from import_export.admin import ImportExportModelAdmin

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('p_name', 'start_date', 'end_date', 'client')
    search_fields = ('client', 'p_name')

    # fieldsets = (
    #     (None, {
    #         'fields': ('cars', 'date')
    #     }),
    #     ('Availability', {
    #         'fields': ('status', 'due_back', 'reader')
    #     }),
    # )
    

class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'company')

class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'position')

# Register your models here.
admin.site.register(Project)
admin.site.register(Client, ClientAdmin)
admin.site.register(Employee)
admin.site.register(Work)
admin.site.register(Invoice)


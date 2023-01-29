from django.db import models
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin

class Project(models.Model):
    p_name = models.CharField('Project Name', max_length=200)
    start_date = models.DateField('Start date', null=True, blank=True)
    end_date = models.DateField('End date', null=True, blank=True)
    client = models.ForeignKey('Client', on_delete=models.SET_NULL, null=True)
    # project_manager = models.ForeignKey('Project manager', on_delete=models.SET_NULL, null=True)
    employee = models.ForeignKey('Employee', on_delete=models.SET_NULL, null=True)
    work = models.ForeignKey('Work', on_delete=models.SET_NULL, null=True)
    invoice = models.ForeignKey('Invoice', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.p_name
    
class Client(models.Model):
    name = models.CharField('Name', max_length=200)
    surname = models.CharField('Surname', max_length=200)
    company = models.CharField('Company', max_length=200)
    email = models.CharField('Email', max_length=200)
    phone = models.CharField('Phone', max_length=200)

    def __str__(self):
        return f'{self.name} {self.surname} {self.company}'
    
class Employee(models.Model):
    name = models.CharField('Name', max_length=200)
    surname = models.CharField('Surname', max_length=200)
    position = models.CharField('Surname', max_length=200)

class Work(models.Model):
    title = models.CharField('Title', max_length=200)
    note = models.CharField('Note', max_length=200)

class Invoice(models.Model):
    formating_date = models.DateField('Formating Date', null=True, blank=True)
    amount = models.FloatField('Amount', max_length=11)

class ClientAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass           

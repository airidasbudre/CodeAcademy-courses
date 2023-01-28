from django.db import models

class Project(models.Model):
    name = models.CharField('Name', max_length=200)
    start_date = models.DateField('Start date', null=True, blank=True)
    end_date = models.DateField('End date', null=True, blank=True)
    client = models.ForeignKey('Client', on_delete=models.SET_NULL, null=True)
    project_manager = models.ForeignKey('Project manager', on_delete=models.SET_NULL, null=True)
    employees = models.ForeignKey('Employees', on_delete=models.SET_NULL, null=True)
    


    def __str__(self):
        return self.name

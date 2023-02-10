from django import forms
from .models import Task
from django.contrib.auth.models import User


class MyDateTimeInput(forms.DateTimeInput):
    input_type = "datetime-local"

class TaskCreateUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['text', 'user']
        widgets = {"date": forms.widgets.DateTimeInput(attrs={'type': 'datetime-local'})}
        # widgets = {"terminas": MyDateTimeInput()}


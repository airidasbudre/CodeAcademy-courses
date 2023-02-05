from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    text = models.TextField(verbose_name="Text", max_length=1000)
    user = models.ForeignKey(to=User, verbose_name="User", on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField("Date", auto_now_add=True)

    def __str__(self):
        return f'{self.text} {self.date}'



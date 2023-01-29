from django.urls import path

from . import views
from .views import home

urlpatterns = [
    # path('', views.index, name='index'),
    path('', home, name='home'),

]
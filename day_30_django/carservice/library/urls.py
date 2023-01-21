from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('service/', views.ServiceListView.as_view(), name='service'),
    path('car/', views.cars, name='car'),                                               
]
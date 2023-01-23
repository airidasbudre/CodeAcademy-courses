from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('service/', views.ServiceListView.as_view(), name='service'),                                            
    path('cars/', views.cars, name='cars'),          
    path('cars/<int:car_id>', views.car, name='car'),    
    path('employees/', views.EmployeesListView.as_view(), name='employees'),                                   
]
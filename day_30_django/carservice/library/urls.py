from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),                                           
    path('cars/', views.cars, name='cars'),     
    path("orders/", views.OrderListView.as_view(), name="orders"),   
    path("orders/<int:pk>", views.OrderDetailView.as_view(), name="order"),  
    path('cars/<int:car_id>', views.car, name='car'),   
    path('search/', views.search, name='search'), 
    path('employees/', views.EmployeesListView.as_view(), name='employees'),     
    path("myorders/", views.UserOrderListView.as_view(), name="my_order"),
    path('profile/', views.profile, name='profile')                              
]
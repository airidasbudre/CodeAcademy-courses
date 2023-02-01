from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),                                           
    path('cars/', views.cars, name='cars'),     
    path('cars/<int:car_id>', views.car, name='car'),   
    path('service/', views.Service, name='service'), 
    path("orders/", views.OrderListView.as_view(), name="orders"),   
    path("orders/<int:pk>", views.OrderDetailView.as_view(), name="order"),  
    path('search/', views.search, name='search'), 
    path('employees/', views.EmployeesListView.as_view(), name='employees'),     
    path("myorders/", views.UserOrderListView.as_view(), name="my_orders"),
    path('profile/', views.profile, name='profile'),        
    path('register/', views.register, name='register'),      
    path("orders/create", views.OrderCreateView.as_view(), name="order_create"),
    path('orders/<int:pk>/edit', views.UserOrderUpdateView.as_view(), name="order_edit"),
    path('orders/<int:pk>/delete', views.UserUsakymasDeleteView.as_view(), name="order_delete"),                
]
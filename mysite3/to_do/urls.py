from django.urls import path, include
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', views.index, name='index'),   
    path('accounts/', include('django.contrib.auth.urls')),
    path('tasks/', login_required(views.view_tasks), name='tasks'),
    
]
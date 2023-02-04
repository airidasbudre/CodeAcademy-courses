from django.urls import path
from . import views
from .views import ProjectsView, HomePageView, AboutPageView

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('projects/', views.ProjectsView.as_view(), name='projects'),
    path('about/', AboutPageView.as_view(), name='about'),

]

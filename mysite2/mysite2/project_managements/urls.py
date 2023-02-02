from django.urls import path
from . import views
from .views import ProjectsView, HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('projects/', ProjectsView.as_view(), name='projects'),

]
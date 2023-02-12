from django.urls import path, include
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', views.index, name='index'),   
    path('accounts/', include('django.contrib.auth.urls')),
    path('tasks/', login_required(views.view_tasks), name='tasks'),
    path("tasks/create", login_required(views.create_task), name="create"),
    path('tasks/<int:task_id>/edit_task', login_required(views.edit_task), name='edit_task'),
    path('tasks/<int:task_id>/delete_task', login_required(views.delete_task), name='delete_task'),
]
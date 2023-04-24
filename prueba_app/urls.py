from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('hello/<str:username>', views.hello, name='hello'),
    path('projects/', views.projects, name='projects'),
    #path('tasks/<int:id>', views.tasks, name='tasks'),
    path('tasks', views.tasks, name='tasks'),
    path('create_task/', views.create_task, name='create_task'),
    path('create_projects/', views.create_projects, name='create_projects'),
    path('projects/<int:id>', views.project_detail, name='project_detail'),
]
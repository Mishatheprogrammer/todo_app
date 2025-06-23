from django.urls import path
from . import views

urlpatterns = [
    path('addTask/', views.add_task, name='add_task'),

]
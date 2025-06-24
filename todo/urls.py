from django.urls import path
from . import views

urlpatterns = [
    path('addTask/', views.add_task, name='add_task'),
    path('markDone/<int:pk>/', views.mark_as_done, name='mark_done'),
    path('markUnDone/<int:pk>/', views.mark_as_undone, name="undone"),
    path('editTask/<int:pk>/', views.edit_task, name="edit_task"),
    path('deleteTask/<int:pk>/', views.delete_task, name='delete_task')
]
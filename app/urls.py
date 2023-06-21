from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('addTask/',views.addTask,name='addTask'),
    path('mark_as_done/<int:pk>',views.mark_as_done,name='mark_as_done'),
    path('deleteTask/<int:pk>',views.deleteTask,name='deleteTask'),
    path('editTask/<int:pk>',views.editTask,name='editTask')
]

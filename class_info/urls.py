from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('time_table/', views.time_table, name='time_table'),
    path('classes_list/', views.classes_list, name='class_list')
]

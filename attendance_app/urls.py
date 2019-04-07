from django.contrib import admin
from django.urls import path, include
import datetime
from . import views
now = datetime.datetime.now()
today = now.date
urlpatterns = [
    path('today', views.todays_attendance, name='attendace_list')
]

from django.contrib import admin
from django.urls import path, include
import datetime
from . import views
now = datetime.datetime.now()
today = now.date
urlpatterns = [
    path('', views.todays_attendance, name='todays_attendace_list')
]

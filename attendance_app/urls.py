from django.contrib import admin
from django.urls import path, include
import datetime
from . import views
now = datetime.datetime.now()
today = now.date
urlpatterns = [
<<<<<<< HEAD
    path('', views.todays_attendance, name='todays_attendace_list')
=======
    path('today', views.todays_attendance, name='attendace_list')
>>>>>>> d958ff74858b43165c27efe1eefaf78f3cb68c0e
]

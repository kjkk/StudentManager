from django.urls import path
from . import views
urlpatterns = [
    path("student", views.student_profile),
    path("teacher", views.teacher_profile),
<<<<<<< HEAD
    path("", views.HOD_profile),
=======
    path("HOD", views.HOD_profile),
    path("principle", views.principle_profile)
>>>>>>> d958ff74858b43165c27efe1eefaf78f3cb68c0e

]
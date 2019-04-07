from django.urls import path
from . import views
urlpatterns = [
    path("student", views.student_profile),
    path("teacher", views.teacher_profile),
    path("HOD", views.HOD_profile),
    path("principle", views.principle_profile)

]
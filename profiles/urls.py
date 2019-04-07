from django.urls import path
from . import views
urlpatterns = [
    path("student", views.student_profile),
    path("teacher", views.teacher_profile),
    path("", views.HOD_profile),

]
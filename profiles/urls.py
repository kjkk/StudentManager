from django.urls import path
from . import views

urlpatterns = [
    path("student_profile", views.student_profile, name='student_profile'),
    path("teacher_profile", views.teacher_profile, name='teacher_profile'),
    path('add_teacher', views.addTeacher, name='addTeacher')
]

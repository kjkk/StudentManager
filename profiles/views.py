from django.shortcuts import render
from profiles.forms import AddTeacher

# This function renders to student profile page
def student_profile(req):
    return render(req, 'profiles/about_student.html')

#This functin renders to teacher profile page
def teacher_profile(req):
    return render(req,  'profiles/about_faculty.html')

#This function renders to the HOD profile page
def HOD_profile(req):
    return render(req,  'profiles/about_faculty.html')

def addTeacher(req):
    return render(req, 'profiles/add_teacher.html')

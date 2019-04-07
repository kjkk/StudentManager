from django.shortcuts import render

# This function renders to student profile page
def student_profile(req):
    return render(req, 'profiles/about_student.html')

#This functin renders to teacher profile page
def teacher_profile(req):
    return render(req,  'profiles/about_faculty.html')

#This function renders to the HOD profile page
def HOD_profile(req):
    return render(req,  'profiles/about_HOD.html')


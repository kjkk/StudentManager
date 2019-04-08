from django.shortcuts import render

# This function renders to student profile page
def student_profile(req):
<<<<<<< HEAD
    return render(req, 'profiles/about_student.html')

#This functin renders to teacher profile page
def teacher_profile(req):
    return render(req,  'profiles/about_faculty.html')

#This function renders to the HOD profile page
def HOD_profile(req):
    return render(req,  'profiles/about_HOD.html')

=======
    return render(req, 'profiles/student.html')

#This functin renders to teacher profile page
def teacher_profile(req):
    return render(req,  'profiles/teacher.html')

#This function renders to the HOD profile page
def HOD_profile(req):
    return render(req,  'profiles/hod.html')

#This function renders to the principle profile page
def principle_profile(req):
    return render (req, 'profiles/principle.html')
>>>>>>> d958ff74858b43165c27efe1eefaf78f3cb68c0e

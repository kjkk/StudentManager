from django.shortcuts import render
from profiles.forms import AddTeacher

# This function renders to student profile page
def student_profile(req):
    return render(req, 'profiles/about_student.html')

#This functin renders to teacher profile page
def teacher_profile(req):
    return render(req,  'profiles/about_faculty.html')


def addTeacher(req):

    form = AddTeacher()

    print(form)

    if req.method == 'POST':
        form = AddTeacher(req.POST)

        if form.is_valid():
            teacher = form.save(commit=False)
            teacher.save
            return redirect('addTeacher')

    return render(req, 'profiles/add_teacher.html', {'form': form})

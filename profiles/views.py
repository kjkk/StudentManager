from django.shortcuts import render, redirect
from profiles.forms import AddTeacher, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as django_login, authenticate, update_session_auth_hash
from django.contrib import messages


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


def login(request):
    """
    View for user login.
    """
    if request.user.is_authenticated():
    #     user = request.user
    #     print(user.id)
        return redirect('home')
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            django_login(request, user)
            messages.add_message(request, messages.SUCCESS, 'Logged-in successfully')
            try:
                if request.GET.get('next') != '':
                    return redirect(request.GET.get('next'))
            except Exception as e:
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

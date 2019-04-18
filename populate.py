import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'attendance.settings')


import django
django.setup()

import random
from class_info.models import Classes, TimeTable
from profiles.models import Subjects, StudentProfile, TeacherProfile
from faker import Faker

fakegen = Faker()

class_id = ['CS4A2', 'CS4A3', 'CS4B1', 'CS4B2', 'CS4B3', 'CS3B1', 'CS3B2', 'CS3B3', 'CS3A1', 'CS3A2', 'CS3A3']
students = [20, 21, 22]

def add_class():
    classThis=random.choice(class_id)
    t = Topic.objects.get_or_create(class_id=classThis, batch=classThis[-1], sem=classThis[2], section=classThis[3], students=students.random.choice(students))[0]
    t.save()
    return t

deef populate

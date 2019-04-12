from django.db import models
from class_info.models import Classes
# Create your models here.
class StudentProfile(models.Model):
    student_id = models.CharField(max_length = 20)
    roll_no = models.CharField(max_length = 20)
    rtu_roll_no = models.CharField(max_length = 20)
    class_id = models.ForeignKey(Classes, on_delete=models.DO_NOTHING)
    batch = models.CharField(max_length = 20)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    sem = models.CharField(max_length = 50)
    address = models.TextField(max_length = 200)
    dob = models.DateTimeField()
    contact_self = models.CharField(max_length = 12)
    email = models.CharField(max_length = 12)
    contact_father = models.CharField(max_length = 12)

    def __str__(self):
        return self.student_id

class TeacherProfile(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    designation = models.CharField(max_length = 30)
    teacher_id = models.CharField(max_length = 20)
    dob = models.DateTimeField(max_length = 200)
    joining_year = models.DateTimeField()
    address = models.TextField(max_length = 200)
    cc = models.ForeignKey(Classes, blank = True, on_delete= models.CASCADE)

    def __str__(self):
        return self.teacher_id

class Subjects(models.Model):
    subject_id = models.CharField(max_length = 30)
    subject_name = models.CharField(max_length = 50)
    sem = models.CharField(max_length = 50)
    teacher_id = models.CharField(max_length = 20)

    def __str__(self):
        return self.subject_id

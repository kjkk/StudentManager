from django.db import models
from class_info.models import Classes
from profiles.models import StudentProfile , Subjects
from datetime import datetime


class total_attendance(models.Model):
    student_id = models.ForeignKey(StudentProfile, on_delete = models.CASCADE)
    subject_id = models.ForeignKey(Subjects, on_delete = models.CASCADE)
    total_classes = models.IntegerField(max_length=3)
    classes_attended  = models.IntegerField(max_length=2)

    def __str__(self):
        return self.student_id

    
class Attendance(models.Model):
    date = models.DateTimeField(default = datetime.now, blank = True )
    slot1 = models.CharField(max_length = 20)
    slot2 = models.CharField(max_length = 20)
    slot3 = models.CharField(max_length = 20)
    slot4 = models.CharField(max_length = 20)
    slot5 = models.CharField(max_length = 20)
    slot6 = models.CharField(max_length = 20)
    slot7 = models.CharField(max_length = 20)
    student_id = models.ForeignKey(StudentProfile, on_delete = models.CASCADE)
    class_id = models.ForeignKey(Classes, on_delete = models.CASCADE)

    def __str__(self):
        return self.student_id
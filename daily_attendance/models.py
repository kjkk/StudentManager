from django.db import models
# Create your models here.
class DailyAttendance(models.Model):
    studentId = models.CharField(max_length= 8,primary_key = True, unique =True)
    classId = models.CharField(max_length= 3)
    sub1 = models.CharField(max_length= 40, blank = True)
    sub2 = models.CharField(max_length= 40, blank = True)
    sub3 = models.CharField(max_length= 40, blank = True)
    sub4 = models.CharField(max_length= 40, blank = True)
    sub5 = models.CharField(max_length= 40, blank = True)
    sub6 = models.CharField(max_length= 40, blank = True)
    sub6 = models.CharField(max_length= 40, blank = True)
  
    


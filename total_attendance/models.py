from django.db import models

# Create your models here.
class total_attendance(models.Model):
    student_id = models.CharField(max_length  =20)
    sub2 =models.IntegerField(max_length=4)
    sub3 =models.IntegerField(max_length=4)
    sub4 =models.IntegerField(max_length=4)
    sub5 =models.IntegerField(max_length=4)
    sub6 =models.IntegerField(max_length=4)
from django.db import models
# from django.utils import timezone
# Create your models here.
class TimeTable(models.Model):
    day_no = models.IntegerField(max_length = 20)
    day = models.CharField(max_length = 20)
    sub1 = models.CharField(max_length = 20)
    # sub1_time = models.datetime
    class_name = models.CharField(max_length = 20)
    batch = models.CharField(max_length = 20)
    teacher = models.CharField(max_length = 20)
    classroom = models.CharField(max_length = 20)
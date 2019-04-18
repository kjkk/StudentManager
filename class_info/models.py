from django.db import models
# from django.utils import timezone
# Create your models here.

class Classes(models.Model):
    class_id = models.CharField(max_length = 20, unique=True)
    batch = models.CharField(max_length = 20)
    sem = models.IntegerField()
    branch = models.CharField(max_length = 20)
    section = models.CharField(max_length = 20)
    students = models.IntegerField()

    def __str__(self):
        return self.class_id


class TimeTable(models.Model):
    day = models.CharField(max_length = 20)
    slot1 = models.CharField(max_length = 20)
    slot2 = models.CharField(max_length = 20)
    slot3 = models.CharField(max_length = 20)
    slot4 = models.CharField(max_length = 20)
    slot5 = models.CharField(max_length = 20)
    slot6 = models.CharField(max_length = 20)
    slot7 = models.CharField(max_length = 20)
    class_id = models.ForeignKey(Classes, on_delete = models.CASCADE)

    def __str__(self):
        return self.day

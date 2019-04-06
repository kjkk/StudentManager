from django.db import models

# Create your models here.
class student(models.Model):
    student_id = models.CharField(max_length = 20)
    class_name = models.CharField(max_length = 20)
    batch = models.CharField(max_length = 20)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    year = models.CharField(max_length = 50)
    address = models.CharField(max_length = 200)
    contact_self = models.CharField(max_length = 12)
    contact_father = models.CharField(max_length = 12)


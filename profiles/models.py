from django.db import models

# Create your models here.
class StudentProfile(models.Model):
    student_id = models.CharField(max_length = 20)
    class_name = models.CharField(max_length = 20)
    batch = models.CharField(max_length = 20)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    year = models.CharField(max_length = 50)
    address = models.CharField(max_length = 200)
    contact_self = models.CharField(max_length = 12)
    contact_father = models.CharField(max_length = 12)

class TeacherProfile(models.Model):
    name = models.CharField(max_length = 30)
    cc_of = models.CharField(max_length= 30, blank = True)
    cc_of_year = models.CharField(max_length= 30, blank = True)
    
    class1 =  models.CharField(max_length= 30, blank = True)
    sub1 = models.CharField(max_length= 30, blank = True)
    
    class2 =  models.CharField(max_length= 30, blank = True)
    sub2 = models.CharField(max_length= 30, blank = True)

    class3 =  models.CharField(max_length= 30, blank = True)
    sub3 = models.CharField(max_length= 30, blank = True)

    class4 =  models.CharField(max_length= 30, blank = True)
    sub4 = models.CharField(max_length= 30, blank = True)

    class5 =  models.CharField(max_length= 30, blank = True)
    sub1 = models.CharField(max_length= 30, blank = True)

    class6 =  models.CharField(max_length= 30, blank = True)
    sub6 = models.CharField(max_length= 30, blank = True)
    
    class7 =  models.CharField(max_length= 30, blank = True)
    sub7 = models.CharField(max_length= 30, blank = True)
    
    class8 =  models.CharField(max_length= 30, blank = True)
    sub8 = models.CharField(max_length= 30, blank = True)
    
    class9 =  models.CharField(max_length= 30, blank = True)
    sub9 = models.CharField(max_length= 30, blank = True)
    image = models.ImageField()

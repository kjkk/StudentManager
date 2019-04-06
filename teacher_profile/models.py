from django.db import models

# Create your models here.
class teacher(models.Model):
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

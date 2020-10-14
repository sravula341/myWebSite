from datetime import datetime

from django.db import models

# Create your models here.
from django.utils import timezone


class allCourses(models.Model):
    imagename = models.ImageField(upload_to='images/',default='')
    summary = models.CharField(max_length=500,default='')
    coursename = models.CharField(max_length=200)
    instructorname = models.CharField(max_length=200)
    startedfrom = models.DateTimeField('started from')

    def __str__(self):
        return self.coursename

    def was_publixhed_recently(self):
       return self.startedfrom>=timezone.now()-datetime.timedelta(days=1)


class details(models.Model):
    course = models.ForeignKey(allCourses,on_delete=models.CASCADE);
    ct = models.CharField(max_length=500)
    your_Choice = models.BooleanField(default=False)

    def __str__(self):
        return str(self.ct)

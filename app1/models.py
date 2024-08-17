from django.db import models

# Create your models here.
class semres(models.Model):
   
    studentname=models.CharField(max_length=20)
    pinno=models.CharField(max_length=20)
    marks=models.IntegerField()
    college=models.CharField(max_length=20)

    def __str__(self):
        return self.studentname
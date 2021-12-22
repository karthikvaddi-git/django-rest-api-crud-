from django.db import models

# Create your models here.

class student(models.Model):
    studentid=models.CharField(max_length=20, primary_key=True)
    studentname=models.CharField(max_length=30)
    studentage=models.IntegerField()

    def __str__(self):
        return self.studentname


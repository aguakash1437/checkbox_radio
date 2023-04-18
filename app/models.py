from django.db import models

# Create your models here.
class Course(models.Model):
    cno=models.IntegerField()
    cname=models.CharField(max_length=100,primary_key=True)
    tname=models.CharField(max_length=100)

    def __str__(self):
        return self.cname
    
class Student(models.Model):
    sno=models.IntegerField()
    sname=models.CharField(max_length=100)
    cname=models.ForeignKey(Course,on_delete=models.CASCADE)

    def __str__(self):
        return self.sname
















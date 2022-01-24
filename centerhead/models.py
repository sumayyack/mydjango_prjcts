from django.db import models

# Create your models here.
class Course(models.Model):
    course_name=models.CharField(max_length=120,unique=True)
    active_status=models.BooleanField(default=True)

    def __str__(self):
        return self.course_name

class Batch(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    batch_name=models.CharField(max_length=120,unique=True)
    active_status=models.BooleanField(default=True)

class Employee(models.Model):
    email=models.EmailField(max_length=120)
    phone=models.CharField(max_length=12)
    role=models.CharField(max_length=120)

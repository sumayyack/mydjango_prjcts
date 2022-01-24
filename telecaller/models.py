from django.db import models
from centerhead.models import Course
from drs.models import MyUser
# Create your models here.
class Enquiries(models.Model):
    student_name=models.CharField(max_length=120)
    contact=models.CharField(max_length=120)
    email=models.EmailField()
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    options=(
        ("admitted","admitted"),
        ("not-interested","not-interested"),
        ("followup","followup")
    )
    status=models.CharField(max_length=30,choices=options,default="followup")
    followup_date=models.DateField(null=True)
    enquiry_date=models.DateField(auto_now_add=True)
    created_by=models.ForeignKey(MyUser,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.student_name
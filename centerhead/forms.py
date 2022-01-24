from django.forms import ModelForm
from centerhead.models import Course,Batch
from drs.models import MyUser
class CourseForm(ModelForm):
    class Meta:
        model =Course
        fields=["course_name"]

class BatchForm(ModelForm):
    class Meta:
        model =Batch
        fields=["course","batch_name"]


class EmployeeForm(ModelForm):
    class Meta:
        model=MyUser
        fields=["email","phone","role","password"]
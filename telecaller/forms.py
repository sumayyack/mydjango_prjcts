from django import forms
from telecaller.models import Enquiries

class LoginForm(forms.Form):
    email=forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))


class EnquiryForm(forms.ModelForm):
    class Meta:

        model= Enquiries
        #fields=[
        #    "student_name",
        #    "contact",
        #    "email",
        #    "course",
        #    "status",
        #    "followup_date"
        #]
        exclude=("enquiry_date","created_by")
        widgets={
            "followup_date":forms.DateInput(attrs={"type":"date"})
        }

class DateFilterForm(forms.Form):
    from_date=forms.DateField(widget=forms.DateInput(attrs={"type":"date"}))
    to_date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
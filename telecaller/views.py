from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,ListView
from telecaller import forms
from django.contrib.auth import authenticate,login
from telecaller.models import Enquiries
from django.urls import reverse_lazy
from datetime import date
# Create your views here.



class SignInView(TemplateView):
    def get(self, request, *args, **kwargs):
        form=forms.LoginForm()
        return render(request,"login.html",{"form":form})
    def post(self,request):
        form=forms.LoginForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data["email"]
            password=form.cleaned_data["password"]
            user=authenticate(request,username=email,password=password)
            if user:
                login(request,user)
                if request.user.role=="telecaller":
                    return render(request,"telecaller_home.html")
                else:

                    return redirect("centerheadhome")

class BaseHome(TemplateView):
    template_name = "base.html"

class TelecallerHome(TemplateView):
    template_name = "telecaller_home.html"

class EnquiryCreate(CreateView):
    model = Enquiries
    form_class = forms.EnquiryForm
    template_name = "add_enquiries.html"
    success_url = reverse_lazy("home")

    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            enquiry=form.save(commit=False)
            enquiry.created_by=request.user
            enquiry.save()
            return redirect("home")

class EnquiryList(ListView):
    model= Enquiries
    template_name = "enquiry_list.html"
    context_object_name = "enquiries"
    def get_queryset(self):
        user=self.request.user
        return self.model.objects.filter(created_by=user)

class Followups(ListView):
    template_name = "followups.html"
    model= Enquiries
    context_object_name = "followups"
    def get_queryset(self):
        user=self.request.user
        return self.model.objects.filter(created_by=user,followup_date=date.today())

class ReportView(ListView):
    template_name = "reports.html"
    model=Enquiries
    context_object_name = "reports"
    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        user=self.request.user
        count=self.model.objects.filter(created_by=user,enquiry_date=date.today()).count()
        context["reports"]=count
        #admission_count=self.model.objects.filter(enquiry_date=date.today(),created_by=user,status="admitted").count()
        #context["admission_count"]=admission_count
        form=forms.DateFilterForm()
        context["form"]=form
        return context
    def post(self,request,*args,**kwargs):
        form=forms.DateFilterForm(request.POST)
        if form.is_valid():
            from_date=form.cleaned_data["from_date"]
            to_date=form.cleaned_data["to_date"]
            admission_count=Enquiries.objects.filter(created_by=request.user,
                                                    status="admitted",
                                                    enquiry_date__range=[from_date,to_date]).count()
            print("admission_count=======",admission_count)
            enq_count=Enquiries.objects.filter(created_by=request.user,
                                              enquiry_date__range=[from_date,to_date]).count()
            print("enq_date========",enq_count)
            context={}
            context["admission_count"]=admission_count
            context["enq_count"]=enq_count
            form=forms.DateFilterForm()
            context["form"]=form
            return render(request,self.template_name,context)



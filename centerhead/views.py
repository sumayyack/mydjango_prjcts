from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,UpdateView
from centerhead.forms import CourseForm,BatchForm,EmployeeForm
from centerhead.models import Course,Batch
from django.urls import reverse_lazy
from drs.models import MyUser
# Create your views here.
class AdminHome(TemplateView):
    template_name = "centerhead/adminhome.html"


class CourseAdd(CreateView):
    model = Course
    form_class =CourseForm
    template_name = "centerhead/addcourse.html"
    success_url = reverse_lazy("addcourse")

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["courses"]=self.model.objects.all()
        return context


#class Courses(ListView):
#    template_name = "centerhead/courses.html"
#    model = Course
#    context_object_name = "courses"

class Batches(CreateView):
    form_class = BatchForm
    template_name = "centerhead/batches.html"
    model = Batch
    success_url = reverse_lazy("batches")

    def get_context_data(self, **kwargs):
        context=super().get_context_data()
        context["batches"]=self.model.objects.all()
        return context


class Employees(CreateView):
    model= MyUser
    template_name = "centerhead/employees.html"
    form_class = EmployeeForm
    success_url = reverse_lazy("employees")
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["employees"]=self.model.objects.all()
        return context
    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            employee=form.save(commit=False)
            emp=MyUser.objects.create_user(email=employee.email,phone=employee.phone,role=employee.role,password=employee.password)
            emp.save()
            return redirect("employees")


class CourseUpdateView(UpdateView):
    model = Course
    template_name = "centerhead/course_edit.html"
    form_class = CourseForm
    pk_url_kwarg = "id"
    success_url = reverse_lazy("addcourse")

class EmployeeEditView(UpdateView):
    model = MyUser
    template_name = "centerhead/employee_update.html"
    form_class = EmployeeForm
    pk_url_kwarg = "id"
    success_url =reverse_lazy("employees")
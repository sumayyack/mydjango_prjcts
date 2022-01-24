from django.urls import path
from centerhead import views

urlpatterns=[
    path("",views.AdminHome.as_view(),name="centerheadhome"),
    path("courses",views.CourseAdd.as_view(),name="addcourse"),
    path("courses/edit/<int:id>",views.CourseUpdateView.as_view(),name="editcourse"),
    path("batches",views.Batches.as_view(),name="batches"),
    path("employees",views.Employees.as_view(),name="employees"),
    path("employees/change/<int:id>",views.EmployeeEditView.as_view(),name="updateemployee"),

]
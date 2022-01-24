from django.urls import path
from telecaller import views

urlpatterns=[
    path("home",views.BaseHome.as_view(),name="basehome"),
    path("",views.TelecallerHome.as_view(),name="home"),
    path("login",views.SignInView.as_view(),name="signin"),
    path("enquiries/add",views.EnquiryCreate.as_view(),name="addenquiries"),
    path("enquiries",views.EnquiryList.as_view(),name="enquiries"),
    path("followups",views.Followups.as_view(),name="followups"),
    path("reports",views.ReportView.as_view(),name="report")
]
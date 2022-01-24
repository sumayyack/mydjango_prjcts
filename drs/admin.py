from django.contrib import admin

# Register your models here.
from drs.models import MyUser
admin.site.register(MyUser)
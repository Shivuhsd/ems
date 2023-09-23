from django.contrib import admin
from .models import StudentCSV, StudentData, OTP

# Register your models here.

admin.site.register(StudentCSV)
admin.site.register(StudentData)
admin.site.register(OTP)

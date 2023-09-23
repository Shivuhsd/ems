from django.contrib import admin
from .models import StudentCSV, Time_Table, StudentData, Student_data, OTP, Room, Add_Staff, Subjects, Link, Dept, Elective, Subject_Student_link

# Register your models here.

admin.site.register(StudentCSV)
admin.site.register(StudentData)
admin.site.register(OTP)
admin.site.register(Subjects)
admin.site.register(Link)
admin.site.register(Add_Staff)
admin.site.register(Room)
admin.site.register(Dept)
admin.site.register(Elective)
admin.site.register(Subject_Student_link)
admin.site.register(Student_data)
admin.site.register(Time_Table)
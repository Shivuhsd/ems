from django.db import models

# Create your models here.


#Department
class Dept(models.Model):
    name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class StudentData(models.Model):
    usn = models.CharField(max_length=20, null=False)
    name = models.CharField(max_length=100, null=False)
    father_name = models.CharField(max_length=100, null=False)
    mother_name = models.CharField(max_length=100, null=False)
    dept_name = models.CharField(max_length=100, blank=True)
    course = models.CharField(max_length=100, null=False)
    dob = models.DateField()
    mobile = models.CharField(max_length=12, null=False)
    sem = models.IntegerField(blank=False)


class StudentCSV(models.Model):
    file_name = models.CharField(max_length=100, null=True)
    csv_file = models.FileField(upload_to='student_csv/')



#model for OTP
class OTP(models.Model):
    otp = models.CharField(max_length=10)
    otp_usn = models.CharField(max_length=100, null=False)


#model for Room
class Room(models.Model):
    room_number = models.CharField(max_length=4, blank=True)
    capacity = models.IntegerField(blank=True)


    def __str__(self):
        return self.room_number
    



#model for Adding Staff
class Add_Staff(models.Model):
    name = models.CharField(max_length=100, blank=True)
    dept = models.ForeignKey(Dept, on_delete=models.CASCADE)


    def __str__(self):
        return self.name
    

#model to Link Students, Staff, Room
class Link(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    student = models.ForeignKey(StudentData, on_delete=models.CASCADE)
    staff = models.ForeignKey(Add_Staff, on_delete=models.CASCADE)


#Model for Subjects
class Subjects(models.Model):
    sub_code = models.CharField(max_length=32, blank=True)
    sub_name = models.CharField(max_length=199, blank=True)
    dept = models.ForeignKey(Dept, on_delete=models.CASCADE)
    types = models.CharField(max_length=100, blank=True)
    sem = models.IntegerField(blank=False)

    def __str__(self):
        return self.sub_code + "----" + self.sub_name
    


#model To Store Elective
class Elective(models.Model):
    code = models.CharField(max_length=100, blank=True)
    subname = models.CharField(max_length=100, blank=True)
    dept = models.ForeignKey(Dept, on_delete=models.CASCADE)
    seme = models.IntegerField(blank=False)


    def __str__(self):
        return self.code + "----------" + self.subname

#model to define which student have opted for which subject
class Subject_Student_link(models.Model):
    stu = models.ForeignKey(StudentData, on_delete=models.CASCADE)
    sub = models.ForeignKey(Elective, on_delete=models.CASCADE)


##
class Student_data(models.Model):
    u_id = models.ForeignKey(StudentData, on_delete=models.CASCADE, blank=False)
    elective = models.ForeignKey(Elective, on_delete=models.CASCADE, blank=False)
    photo = models.ImageField(blank=False, upload_to='p_photo/')



### Time Table

class Time_Table(models.Model):
    date = models.DateField(blank=False)
    sub_code = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    Time = models.TimeField(blank=False)
    detp = models.ForeignKey(Dept, on_delete=models.CASCADE)


    def __str__(self):
        return self.sub_code + "   " + self.date

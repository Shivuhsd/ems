from django.db import models

# Create your models here.

class StudentData(models.Model):
    usn = models.CharField(max_length=20, null=False)
    name = models.CharField(max_length=100, null=False)
    father_name = models.CharField(max_length=100, null=False)
    mother_name = models.CharField(max_length=100, null=False)
    dept_name = models.CharField(max_length=100, null=False)
    course = models.CharField(max_length=100, null=False)
    dob = models.DateField()
    mobile = models.CharField(max_length=12, null=False)


class StudentCSV(models.Model):
    file_name = models.CharField(max_length=100, null=True)
    csv_file = models.FileField(upload_to='student_csv/')



#model for OTP
class OTP(models.Model):
    otp = models.CharField(max_length=10)
    otp_usn = models.CharField(max_length=100, null=False)
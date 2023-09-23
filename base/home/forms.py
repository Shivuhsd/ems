from . models import StudentCSV, OTP, Student_data
from django import forms

class CSV_S(forms.ModelForm):
    class Meta:
        model = StudentCSV
        fields = ['file_name','csv_file']


class OTP_OTP(forms.ModelForm):
    class Meta:
        model = OTP
        fields = '__all__'

class Student(forms.ModelForm):
    class Meta:
        model = Student_data
        fields = ['elective', 'photo']
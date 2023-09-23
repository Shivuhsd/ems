from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . models import StudentData, StudentCSV, OTP
import csv
from . forms import CSV_S, OTP_OTP
import os
from .sendingmail import Sending_Mail
from .custom import GenerateOTP
from django.contrib.auth.models import User

# Create your views here.

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Check Your Credentials")
            
        # Return an 'invalid login' error message.
        ...
    return render(request, 'login.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def StudentUpload(request):
    form = CSV_S()
    if request.method == 'POST':
        file_csv = CSV_S(request.POST, request.FILES)
        if file_csv.is_valid():
            obj = file_csv.save()
            name_file = obj.id

            
            file_name = StudentCSV.objects.get(id = name_file)
           
            
            path_csv = os.path.join('media', file_name.csv_file.name)

            with open(path_csv, 'r') as file:
                csv_file = csv.DictReader(file)
                for row in csv_file:
                    usn = row['USN']
                    name = row['Name']
                    father_name = row['Father Name']
                    mother_name = row['Mother Name']
                    phone = row['Phone']
                    dob = row['DOB']
                    dept = row['Department']
                    course = row['Course']

                    data = StudentData(usn=usn, name = name, father_name = father_name, mother_name = mother_name, dept_name = dept, mobile = phone, dob = dob, course = course)
                    data.save()
        else:
            messages.error(request, "SomeThing Went Wrong")

    
        
    return render(request, 'supload.html', {'form':form})



def ShowUpload(request):
    return render(request, 'showupload.html')


def Validate(request):
    if request.method == 'POST':
        usn = request.POST['usn']
        phone = request.POST['phone']

        try:
            form = StudentData.objects.get(usn = usn, mobile = phone)
            pk = form.id
            return redirect('emailveri', pk=pk)
        except:
            messages.error(request, "Check Your Credentials")

    return render(request, 'validate.html')


def EmailVeri(request, pk):
    if request.method =='POST':
        e_mail = request.POST['mail']

        form = StudentData.objects.get(id = pk)

        #Storing the Generated OTP To Database
        otp = GenerateOTP()

        OTP(otp=otp, otp_usn=form.usn).save()

        subject = "OTP Verification"
        message = "Hi " + form.name + '\n' + form.usn + "\n\n" + "Your OTP is  " + otp
        try:
            Sending_Mail(subject, message, e_mail)
            return redirect("otpverify", pk=form.usn)
        except:
            messages.error(request, "Something Went Wrong")

    return render(request, 'emailveri.html')

def OtpVerify(request, pk):
    if request.method == 'POST':
        otp = request.POST['otp']

        data = OTP.objects.get(otp=otp, otp_usn = pk)

        if data:
            messages.success(request, "Verification Success")
            da = data
            data.delete()
            return redirect('password', pk=da.otp_usn)
        else:
            messages.error(request, "OTP Verification Failed")
    return render(request, 'otp.html')


def Password(request, pk):
    data = StudentData.objects.get(usn=pk)
    if request.method == 'POST':
        pass_word1 = request.POST['password1']
        pass_word2 = request.POST['password2']

        if pass_word1 != pass_word2:
            messages.error(request, 'Passwords Dont Match')
        else:
            user = User.objects.create_user(data.usn, data.email, pass_word1)
            user.first_name = data.name
            user.save()
            login(request, user)
            return redirect('dashboard')
    return render(request, 'password.html', {'data':data})

#
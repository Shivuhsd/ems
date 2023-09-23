from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . models import StudentData, StudentCSV, Student_data, Add_Staff, OTP, Subjects, Dept, Elective, Room
import csv
from . forms import CSV_S, OTP_OTP, Student
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
            return redirect("otpverify", pk=form.usn, e_mail=e_mail)
        except:
            messages.error(request, "Something Went Wrong")

    return render(request, 'emailveri.html')

def OtpVerify(request, pk, e_mail):
    if request.method == 'POST':
        otp = request.POST['otp']

        data = OTP.objects.get(otp=otp, otp_usn = pk)

        if data:
            messages.success(request, "Verification Success")
            da = data
            data.delete()
            return redirect('password', pk=da.otp_usn, e_mail=e_mail)
        else:
            messages.error(request, "OTP Verification Failed")
    return render(request, 'otp.html')


def Password(request, pk, e_mail):
    data = StudentData.objects.get(usn=pk)
    if request.method == 'POST':
        pass_word1 = request.POST['password1']
        pass_word2 = request.POST['password2']

        if pass_word1 != pass_word2:
            messages.error(request, 'Passwords Dont Match')
        else:
            user = User.objects.create_user(data.usn, e_mail, pass_word1)
            user.first_name = data.name
            user.save()
            login(request, user)
            return redirect('dashboard')
    return render(request, 'password.html', {'data':data, 'email':e_mail})

#DashBoard Examination View
def Dash_Examination(request):
    return render(request, 'admins/dash_Examination.html')



#Dashboard Admin add staff view
def Dash_Admin_Add_Staff(request):
    dept = Dept.objects.all()
    if request.method == 'POST':
        dept = request.POST['dept']
        name = request.POST['name']

        depts = Dept.objects.get(name=dept)

        data = Add_Staff(name = name, dept = depts)

        data.save()

        messages.success(request, 'Staff Added Succesfully')
    return render(request, 'admins/dash_admin_addstaff.html', {'dept': dept})


#Dashboard Admin add Subjects View



#Dashboard Admin HallTicket Generation
def AdminHallticket(request):
    dept = Dept.objects.all()
    subs = None
    ele = ""
    if request.method == 'POST':
        detp = request.POST['dept']
        typs = request.POST['type']

        dt = Dept.objects.get(name=detp)

        if typs == 'core':
            subs = Subjects.objects.filter(types=typs, dept = dt)
        elif typs == 'elective':
            su = Elective.objects.filter(dept = dt)
            for i in su:
                ele = ele +"----" + i.subname

           
            


    return render(request, 'admins/hallticket.html', {'dept': dept, 'subs':subs, 'ele':ele})


#Dashboard Student Hall Ticket View
def Dash_Admin_HallTicketGeneration(request):
    return render(request, 'student/dash_admin_hallticket.html')

#Dashborad for Adding Subjects
def Add_Subject(request):
    dept = Dept.objects.all()
    if request.method == 'POST':
        sub_code = request.POST['sub_code']
        sub_name = request.POST['sub_name']
        sub_dept = request.POST['dept']
        sub_type = request.POST['type']

        depts = Dept.objects.get(name=sub_dept)

        data = Subjects(sub_code = sub_code, sub_name=sub_name, dept=depts, types=sub_type)
        data.save()

        if sub_type == 'elective':
            data = Elective(code = sub_code, subname = sub_name, dept = depts)
            data.save()

        messages.success(request, "Subject Added Succesfully")
    return render(request, 'admins/dash_admin_subjects.html', {'dept': dept})


###
def Add_Room(request):
    if request.method == 'POST':
        num = request.POST['num']
        cap = request.POST['capacity']

        data = Room(room_number = num, capacity = cap)
        data.save()

        messages.success(request, 'Room Added Successfully')
        
    return render(request, 'admins/dash_admin_room.html')


###Profile

def Profile(request):
    form = Student()
    data = StudentData.objects.get(usn = request.user.username)
    photo = None
    try:
        photo = Student_data.objects.get(u_id=data)
    except:
        pass
    if request.method == 'POST':
        data = Student(request.POST, request.FILES)
        if data.is_valid():
            obj = data.save(commit=False)
            i___id = request.user.username
            dat = StudentData.objects.get(usn = i___id)
            obj.u_id = dat
            obj.save()
            messages.success(request, 'Updated Successfully')
            return redirect('profile')
        else:
            messages.error(request, 'Something Went Wrong')
    return render(request, 'student/profile.html', {'data':data, 'form':form, 'photo':photo})
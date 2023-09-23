from django.urls import path
from . import views

urlpatterns = [
    path('', views.LoginPage, name='loginpage'),

    path('dashboard/', views.dashboard, name='dashboard'),

    path('studentupload/', views.StudentUpload, name='studentupload'),

    path('showupload/<str:pk>/', views.ShowUpload, name='showupload'),

    path('validate/', views.Validate, name='validate'),

    path('emailveri/<str:pk>/', views.EmailVeri, name='emailveri'),

    path('otpverify/<str:pk>/<str:e_mail>/', views.OtpVerify, name='otpverify'),

    path('password/<str:pk>/<str:e_mail>/', views.Password, name='password'),

    #Dash Examination Path/URL
    path('Dash_Examination/', views.Dash_Examination, name='dash_examination'),

    #Dash HallTicket Generation Path/URL
    path('AdminHallTicket/', views.AdminHallticket, name='admin_HallTicket'),

    #Dash Student HallTicket View
    path('HallTicket/', views.Dash_Admin_HallTicketGeneration, name='dash_admin_HallTicketGeneration'),


    path('addsubjects/', views.Add_Subject, name='addsubject'),
    

    path('addstaff/', views.Dash_Admin_Add_Staff, name='addstaff'),


    path('addroom/', views.Add_Room, name='addroom'),


    path('profile/', views.Profile, name='profile'),
]
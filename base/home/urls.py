from django.urls import path
from . import views

urlpatterns = [
    path('', views.LoginPage, name='loginpage'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('studentupload/', views.StudentUpload, name='studentupload'),
    path('showupload/<str:pk>/', views.ShowUpload, name='showupload'),
    path('validate/', views.Validate, name='validate'),
    path('emailveri/<str:pk>/', views.EmailVeri, name='emailveri'),
    path('otpverify/<str:pk>/', views.OtpVerify, name='otpverify'),
    path('password/<str:pk>/', views.Password, name='password'),
]
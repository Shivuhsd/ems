from django.core.mail import send_mail

def Sending_Mail(subject, message, mail):
  
    send_mail(
            subject,
            message,
            "No Reply@gmail.com",
            [mail],
            fail_silently=False
    )
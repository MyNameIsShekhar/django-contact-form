from django.shortcuts import render
from django.core.mail import send_mail
import smtplib


def index(request):
    try:
        if request.method == "POST":
            message_name = request.POST['message_name']
            message_email = request.POST['message_email']
            message = request.POST['message']

            message = f"Name: {message_name}\nEmail: {message_email}\nMessage: {message}"

            try:
                send_mail(
                    f'New message from {message_name}',
                    message,
                    message_email,
                    ['youremail@gmail.com'],    # Your Email
                    fail_silently=False,
                )
            except smtplib.SMTPException:
                return render(request, 'emailapp/success.html', {'view_name': 'mail_error'})        

            return render(request, 'emailapp/success.html', {'view_name': 'index', 'message_name': message_name, 'message_email': message_email, 'message': message})
        else:
            return render(request, 'emailapp/index.html', {'view_name': 'index'})
    except:
        return render(request, 'emailapp/success.html', {'view_name': 'smth_wrng'})  

  
def redirect_error(request, unknown_path):
    return render(request, 'emailapp/success.html', {'view_name': 'redirect_error'})
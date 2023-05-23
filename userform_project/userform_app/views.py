import re
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from userform_app.models import User
from django.views.generic.base import TemplateView



def validate_phone_number(phone_number):
    mob = str(phone_number)
    m = re.match("(0|91)?[6-9][0-9]{9}", mob)
    return m


def user_form(request):
    if request.method == 'POST':
        name = request.POST['name']
        date_of_birth = request.POST['date_of_birth']
        email = request.POST['email']
        phone_number = request.POST['phone_number']

        if validate_phone_number(phone_number) is None:
            return HttpResponse("Enter a valid phone number !!")
        else:
            try:
                fact = User(name=name, date_of_birth=date_of_birth, email=email, phone_number=phone_number)
                fact.save()
            except Exception as msg:
                return HttpResponse(msg)
            else:
                send_mail(
                    'Form is submitted successfully',
                    f'''Hii! {name},
                    Your form is successfully submitted''',
                    'rk9900999@gmail.com',
                    [email],
                    fail_silently=False,
                )
        data_show = User.objects.all().values()
        return HttpResponse(data_show)

    if request.method == 'GET':
        return render(request, 'user_form.html')

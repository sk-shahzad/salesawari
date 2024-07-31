from django.shortcuts import render, redirect
from django.contrib import messages
from . models import Contact


def home(request):
    return render(request, 'homepage/02_dark-index-2.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('Name')
        email = request.POST.get('Email')
        phone = request.POST.get('Phone')
        message = request.POST.get('Message')

        required_fields = {
            'Name': name,
            'Email Address': email,
            'Message':  message
        }

        for key, value in required_fields.items():
            if not value:
                messages.error(request, f'{key} required field!')
                return redirect('contact')

        contact_instances = Contact.objects.create(name=name, email=email, phone=phone, message=message)
        messages.success(request, "Thank you for contact SaleSawari, we usally reply within a few minutes", )

    return render(request, 'homepage/contact-us.html')


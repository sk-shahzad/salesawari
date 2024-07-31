from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from . models import Account
from django.contrib import messages

def login(request):
    return render(request, 'accounts/login.html')

def register(request):
        if request.method == 'POST':
            full_name = request.POST.get('name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')
            role = request.POST.get('role')

            if password != confirm_password:
                messages.error(request, 'Password does not match')
                return redirect('register')

            required_field = {'Name': full_name,
                                'Email': email,      
                                'Password': password,
                                 'Role': role}
            
            for key, value in required_field.items():
                if not value:
                    messages.error(request,f'{key} required field')
                    return redirect('register')

            is_buyer = role == 'buyer'
            is_seller = role == 'seller'

            user = Account.objects.create(full_name=full_name,email=email,password=password,is_buyer=is_buyer,is_seller=is_seller)
            user.save()

            messages.success(request, 'Account created successfully')
            return redirect('login')
        else:
            return render(request, 'accounts/register.html')

    


        

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from . models import Account
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.urls import reverse
from django.core.exceptions import ValidationError

def registerUser(request, user_type):

        if request.method == 'POST':
            full_name = request.POST.get('name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')
            role = request.POST.get('role')

            if password != confirm_password:
                messages.error(request, 'Password does not match')
                return redirect(reverse('register_user', args=[user_type]))

            required_field = {'Name': full_name,
                               'Email': email,      
                                'Password': password,
                                 'Role': role}
            
            for key, value in required_field.items():
                if not value:
                    messages.error(request,f'{key} required field')
                    return redirect(reverse('register_user', args=[user_type]))

            is_buyer = role == 'buyer'
            is_seller = role == 'seller'
            
            if Account.objects.filter(email=email).exists():
                messages.error(request, 'Email Already exist')
                return redirect(reverse('register_user', args=[user_type]))
            

            user = Account.objects.create(full_name=full_name,email=email,password=make_password(password),is_buyer=is_buyer,is_seller=is_seller)
            user.save()

            messages.success(request, 'Account created successfully')
           
            return redirect('login')
        template = 'accounts/buyer.html' if user_type == 'buyer' else 'accounts/seller.html'
            # return render(request, 'accounts/register.html')
        return render(request, template)



# def seller(request):
#     if request.method == 'POST':
#             full_name = request.POST.get('name')
#             email = request.POST.get('email')
#             password = request.POST.get('password')
#             confirm_password = request.POST.get('confirm_password')
#             role = request.POST.get('role')

#             if password != confirm_password:
#                 print(password)
#                 print(confirm_password)
#                 messages.error(request, 'Password does not match')
#                 return redirect('seller')

#             required_field = {'Name': full_name,
#                                'Email': email,      
#                                 'Password': password,
#                                  'Role': role}
            
#             for key, value in required_field.items():
#                 if not value:
#                     messages.error(request,f'{key} required field')
#                     return redirect('register')


#             user = Account.objects.create(full_name=full_name,email=email,password=make_password(password),is_seller=True)
#             user.save()

#             messages.success(request, 'Account created successfully')
#             return redirect('login')
#     else:
#             # return render(request, 'accounts/register.html')
#          return render(request, 'accounts/seller.html')

def register(request):
    
      return render(request, 'accounts/register.html')


def login_user(request):
    # if request.user.is_authenticated:
    #     return redirect('home') 

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            # messages.success(request, "Login Successful")
            return redirect('home') 
        else:
            messages.error(request, "Invalid Email or Password")
            return redirect('login')  

    return render(request, 'accounts/login.html') 

def logoutUser(request):
    logout(request)
    return redirect('home')

def userProfile(request):
    return render(request, 'accounts/profile.html')


    


        

# from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login, logout

# def loginpage(request):
#     page = 'login'
#     if request.user.authenticated:
#         return redirect('home')
#     if request.method == 'POST':
#         username = request.POST.get('username').lower()
#         password = request.POST.get('password')
#         try:
#             user = User.object.get(username=username)
#         except :
#             message.error(request, 'User does not exist')
        
#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             login(request, user)
#             return redirect ('home')
#         else: 
#             message.error(request, 'Username or password does not exist')
#             return render(request, 'login_register.html', {'page':page})


        

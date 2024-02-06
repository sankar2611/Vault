from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password  # for encryption of password
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import userdetails
# Create your views here.


# def userlogin(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']

#         user =  authenticate(request,username=username, password=password)
       

#         if user is not None and user.is_active:

#             if user.is_superuser:
#                 login(request, user)
#                 return redirect('admin_dashboard')

#             details = userdetails.objects.get(user = user)
        
#             if details.user_type == 'Government':
#                 login(request, user)
#                 return redirect('Government')

#             elif details.user_type == 'Normal':
#                 login(request, user)
#                 return redirect('Normal_page')
            
#         else:
#             msg = "wrong Credentials"
#             return render(request, 'Registration/login.html', {'msg': msg})
#     return render(request, 'Registration/login.html')

from django.contrib import messages

def admin_dashboard(request):
    # admin_dashboard.html needs to be added
    return render(request, 'Admin/home.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(f"Username: {username}")
        print(f"Password: {password}")

        user = authenticate(username=username, password=password)
        print(f"User: {user}")
       
        if user is not None and user.is_active:
            if user.is_superuser:
                login(request, user)
                return redirect('admin_dashboard')
            else:
                try:
                    details = user.userdetails
                    if details.user_type == 'Government':
                        login(request, user)
                        return redirect('Government')
                    elif details.user_type == 'Normal':
                        login(request, user)
                        return redirect('Normal_page')
                except userdetails.DoesNotExist:
                    messages.error(request, "User details not found")
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'Registration/login.html')




def register(request):
    if request.method == 'POST':
        firstName = request.POST['firstName']
        print(firstName)
        lastName = request.POST['lastName']
        username = request.POST['username']  
        email = request.POST['email']
        phone = request.POST.get('phone')
        role = request.POST['role']
        password = request.POST['password']
        
        user = User.objects.create_user(
            username=username,  # Include the username parameter
            email=email,
            first_name=firstName,
            last_name=lastName,
            password=password
        )
        user.save()
        print(user)
        print(f"User created: {user.__dict__}")

        user_details = userdetails(user_id=user.id, user_phone=phone, user_type=role)
        user_details.save()
        print(f"User details created: {user_details.__dict__}")


        return redirect('login_user')
 
    return render(request, 'Registration/register.html')

def index(request):
    return render(request, 'Registration/index.html')

def login_user(request):
    return render(request, 'Registration/login.html')

def Government(request):
    return render(request, 'government/gov.html')

def Normal_page(request):
    return render(request, 'User/userindex.html')


from django.shortcuts import render, redirect, get_object_or_404
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.

# registration function
def registration(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'email already taken')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'username is already taken')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password1)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'password not matching')
            return redirect('register')
    else:
        return render(request, 'registration/register.html')

    

# login function
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
            messages.info(request, 'Logged in successfully')
        else:
            messages.info(request, 'invalid credential')
    else:
        return render(request, 'registration/login.html')

    return render(request, 'registration/login.html')

# logout function
def logout(request):
    auth.logout(request)
    return redirect('home')
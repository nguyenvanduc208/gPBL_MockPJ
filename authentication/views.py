from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.hashers import make_password

# Create your views here.


def login_handle(request):
    if request.method == 'GET':
        return render(request, 'auth/login.html')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.error(request, 'Wrong username or password')
            return redirect('login')


def register(request):
    if request.method == 'GET':
        return render(request, 'auth/register.html')
    if request.method == 'POST':
        data = request.POST
        if data['password'] is not data['re_password']:
            messages.error(
                request, 'Re-entered password is incorrect')
            return redirect('register')
        try:
            user = User.objects.create_user(
                username=data['username'],
                email=data['email'],
                password=data['password'],
                first_name=data['first_name'],
                last_name=data['last_name'],
            )
            user.save()
            messages.success(request, 'Sign Up Success, Please Login')
            return redirect('login')
        except:
            messages.error(
                request, 'Registration failed, please check registration information again')
            return redirect('register')


def log_out(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login')

def change_password(request):
    if request.method == "GET":
        return render(request, 'auth/change_password.html')
    if request.method == "POST":
        username = request.POST.get('username')
        old_password = request.POST.get('password')
        new_password = make_password(request.POST.get('new_password'))

        user = authenticate(request, username=username, password=old_password)

        if user is None:
            messages.error(request, 'Wrong username or password')
            return redirect('change_pass')
        else:
            user_obj = User.objects.get(username=username)
            user_obj.password = new_password
            user_obj.save()
            messages.success(request, 'Change password success')
            return redirect('login')
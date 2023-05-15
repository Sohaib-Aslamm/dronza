from dronzaPanel.forms import UserForm

from django.contrib.auth.models import User, Group

from django.contrib.auth import authenticate, login as auth_login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from dronzaPanel.decorators import unauthenticated_user, admin_only
from django.contrib import messages
from home.definedEmails import *
# Create your views here

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Auth Functions >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


@unauthenticated_user
def UserRegister(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='Customer')
            user.groups.add(group)
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            notify_user_registration(username, email)
            messages.success(request, f'Hey !  {username} your account created successfully')
            return redirect('/user_login')
    else:
        form = UserForm()
    return render(request, 'User_Register.html', {'form': form})
@unauthenticated_user
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/admin')
        else:
            messages.error(request, 'Username or password is incorrect')
    return render(request, 'login.html')

@unauthenticated_user
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/admin')
        else:
            messages.error(request, 'Username or password is incorrect')
    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('/admin')


@login_required(login_url='/user_login')
@admin_only
def user_list(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'admin_user_list.html', context)

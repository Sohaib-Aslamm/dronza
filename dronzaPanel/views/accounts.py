from dronzaPanel.forms import UserForm

from django.contrib.auth.models import User, Group
from dronzaPanel.models import seoTags

from django.contrib.auth import authenticate, login as auth_login, logout
from django.shortcuts import render, redirect

from dronzaPanel.decorators import unauthenticated_user, admin_only, custom_login_required
from django.contrib import messages

# Create your views here

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Auth Functions >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


@unauthenticated_user
def UserRegister(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')

            # Check if the email already exists
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
                return render(request, 'User_Register.html', {'form': form})

            user = form.save()
            group = Group.objects.get(name='Customer')
            user.groups.add(group)

            user = User.objects.get(username=username)

            # send email
            from home.email_and_slack_messages import Communication_Utils, Email_Content
            subject, message, html_message = Email_Content.welcome_email(user)
            Communication_Utils.email_sender(user, subject, message, html_message)

            messages.success(request, f'Hey! {username}, your account has been created successfully')
            return redirect('/user-login')
    else:
        form = UserForm()

    SEOTAGS = seoTags.objects.filter(page='user_register')
    context = {'form': form, 'SEOTAGS': SEOTAGS}
    return render(request, 'User_Register.html', context)


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

    SEOTAGS = seoTags.objects.filter(page='user_login')
    return render(request, 'login.html', {'SEOTAGS': SEOTAGS})


def user_logout(request):
    logout(request)
    return redirect('/user-login')


@custom_login_required
@admin_only
def user_list(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'admin_user_list.html', context)

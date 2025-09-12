from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models, forms

def register_view(request):
    if request.method == 'POST':
        #form = UserCreationForm(request.POST)
        form = forms.CustomRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = forms.CustomRegisterForm()
        #form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})


def auth_login_view(request):
    if request.method == 'POST':
        form = forms.LoginWithCaptchaForm(data=request.POST)
        #form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('users:user_list')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form':form})


@login_required
def user_list_view(request):
    users = models.CustomUser.objects.all()
    #users = User.objects.all()
    return render(request, 'users/user_list.html', {'user_list':users})

def auth_logout_view(request):
    logout(request)
    return ('users:login')


        




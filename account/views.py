from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserLoginForm, UserRegisterationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from post.models import Post


# Create your views here.

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'you login ')
                return redirect('post:all_post')
            else:
                messages.error(request, "user and pass warng", 'warning')

    else:
        form = UserLoginForm()
    return render(request, 'account/login.html', {'form': form})


def user_register(request):
    if request.method == 'POST':
        form = UserRegisterationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(cd['username'], cd['email'], cd['password'])
            login(request, user)
            messages.success(request, 'you registered', 'success')
            return redirect('post:all_post')
    else:
        form = UserRegisterationForm()
    return render(request, 'account/register.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.success(request, 'you logout succesfuly', 'success')
    return redirect('post:all_post')


def user_dashbord(request, user_id):
    user = get_object_or_404(User, id=user_id)
    posts = Post.objects.filter(user=user)
    return render(request, 'account/dashbord.html', {'user': user,'posts':posts})

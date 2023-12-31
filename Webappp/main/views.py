from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='user_login')
def index(request):
    user = User.objects.all()
    print(user)
    return render(request,'index.html',{'user':user})
def display_view(request):
    
    return render(request,'view.html')


def log_out(request):
    logout(request)
    return redirect('user_login')
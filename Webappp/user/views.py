from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate


def user_login(request):
    user = None
    error_message = None
    if request.POST:
        form_name1 = request.POST.get('signup')
        form_name2 = request.POST.get('user')
        form_name3 = request.POST.get('creator')
        if form_name1 == 'signup':
            fullname = request.POST['fullname']
            email = request.POST['mobile']
            password = request.POST['conpassword']
            try:
                user = User.objects.create_user(username=email,password=password)
                return redirect("user")
            except Exception as e:
                error_message = str(e)

        elif form_name2 == 'user':
           pass 



        elif form_name3 == 'creator':
           username = request.POST['username']
           password = request.POST['password']
           user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('index')
        else:
            error_message = "invalid user"

    return render(request,'user.html',{'user':user,"error_message":error_message})


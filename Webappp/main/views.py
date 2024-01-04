from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
from .models import Generaldata


@login_required(login_url='user_login')
def index(request):
    #current user name getting with db query
    current_user = request.user
    user = User.objects.get(username=current_user)
    user_name = user.first_name
    print(user)
    return render(request,'index.html',{'user':user_name})

def display_view(request):
    #current user name getting without db query
    current_user = request.user
    user_name = current_user.first_name
    db_objects = Generaldata.objects.get(id=1)
    tottal_likes = db_objects.heart_Likes
    db_objects = Generaldata.objects.get(id=1)
    tottal_dislikes = db_objects.heart_Dislikes
    return render(request,'view.html',{
        'user':user_name,
        'tottal_likes':tottal_likes,
        'tottal_dislikes': tottal_dislikes,
        })

def log_out(request):
    logout(request)
    return redirect('user_login')
@require_POST
def update_data(request):
    like = (request.POST.get('like'))
    dislike = (request.POST.get('dislike'))
    generaldata_instance = get_object_or_404(Generaldata,id=1)
    current_likes = generaldata_instance.heart_Likes
    current_dislikes = generaldata_instance.heart_Dislikes
    if like:
        # if like :
            like = int(like)
            new_likes = current_likes+1
            generaldata_instance.heart_Likes=new_likes
            generaldata_instance.save()
            db_objects = Generaldata.objects.get(id=1)
            tottal_likes = db_objects.heart_Likes
            Likes = {'current_likes': tottal_likes}
            return JsonResponse(Likes)
        # elif :
        #     like = int(like)
        #     new_likes = current_likes-1
        #     generaldata_instance.heart_Likes=new_likes
        #     generaldata_instance.save()
        #     db_objects = Generaldata.objects.get(id=1)
        #     tottal_likes = db_objects.heart_Likes
        #     Likes = {'current_likes': tottal_likes}
        #     return JsonResponse(Likes)
    elif dislike:
        # if dislike == '1':
            dislike = int(dislike)
            new_dislikes = current_dislikes+1
            generaldata_instance.heart_Dislikes=new_dislikes
            generaldata_instance.save()
            db_objects = Generaldata.objects.get(id=1)
            tottal_dislikes = db_objects.heart_Dislikes
            dislikes = {'current_dislikes': tottal_dislikes}
            return JsonResponse(dislikes)
        # elif like == '0':
        #     like = int(like)
        #     new_dislikes = current_dislikes-1
        #     generaldata_instance.heart_Dislikes=new_dislikes
        #     generaldata_instance.save()
        #     db_objects = Generaldata.objects.get(id=1)
        #     tottal_dislikes = db_objects.heart_Dislikes
        #     dislikes = {'current_dislikes': tottal_dislikes}
        #     return JsonResponse(dislikes)

from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from kick.models import *
from django.contrib.auth.decorators import login_required
# Create your views here.
def signup(request):
    if request.method =='POST':
        username =request.POST['username']
        image = request.FILES['image']
        email = request.POST['email']
        bio =request.POST['bio']
        sex =request.POST['sex']
        first_name =request.POST['first_name']
        last_name =request.POST['last_name']
        password =request.POST['password']
        password2 =request.POST['password2']

        if password==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email ALready exits')
                return redirect('a')

            elif User.objects.filter(username=username).exists():
                messages.info(request,'USer name taken')
                return redirect('a')
            
            else:
                user=User.objects.create_user(username=username,email=email,first_name=first_name,last_name=last_name,password=password)
                messages.info(request,'Congrats succefully created account')
                user.save()
                user_model =User.objects.get(username=username)
                cost1=costummer.objects.create(user=user_model,bio=bio,sex=sex,profile_p=image,id_user=user_model.id)
                cost1.save()
        else:
            messages.info(request,'Password Not matching')
            return redirect('a')
            

    else:
        return render(request,'sigup.html')
    return redirect('a')

@login_required(login_url='/login/')
def dash(request):
    if request.user.is_authenticated:
        profile = costummer.objects.filter(user=request.user).first()
        request.session['profile'] = profile.cos
    return render(request,'dash.html')


def login(request):
    if not request.user.is_authenticated:
        if request.method =='POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)

                return redirect('dash')
            else:
                messages.info(request,'Credentials Invalid')
                return redirect('login')
        else:
            return render(request,'login.html')

    else:
        return redirect('dash')




def logout(request):
    auth.logout(request)
    return redirect('login')




def cos(request):

    am = costummer.objects.get(user=request.user) 
    if am.cos:

        # pro = costummer.objects.filter(user=request.user) 
        return render(request,'pro.html')
    else:
       
        return render(request,'ha.html')

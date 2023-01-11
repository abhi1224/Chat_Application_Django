from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from datetime import datetime 
from .models import *
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/user')
        else:
            messages.info(request,"Invailed user.....!")
            return redirect('/login')
    else:
        return render(request,'login.html')


def chat(request,username):
    users = User.objects.get(username=username)
    print("username....",username)
    return render(request,'chat.html',{'users':users})

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email is already used')
                return redirect('/signup')
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.first_name = firstname
                user.last_name = lastname
                user.save()   
                return redirect('/login')
        else:
            messages.info(request,' Password is not same Please enter correct password')
            return redirect('/signup')
    else:
        return render(request,'signup.html')
    # return render(request,'signup.html')

def user(request):
    users = User.objects.all()
        # print(users)
    return render(request,'user.html',{'users':users})

# def create_room(request): 
#     return render(request,'create_room.html')




def create_room(request):  
    if request.method == 'POST':
        username = request.POST['username']
        name = request.POST['room_name']
        room_name = Room(name = name, username = username)
        room_name.save()
        return redirect('/room/'+name)
    else:
        return render(request,'create_room.html')
    

def room(request,group_name):
    group = Group.objects.filter(name=group_name).first()
    chats=[]
    if group:
        chats = Chat.objects.filter(group=group)        
    else:
        group = Group(name = group_name)
        group.save()
    return render(request,'room.html',{'groupname':group_name, 'chats':chats})


def logout(request):
    auth.logout(request)
    return redirect('/')
from django.shortcuts import render, redirect
from .models import Message, MessageRecipient
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth 
from django.contrib import messages


@login_required(login_url='/register/')
def home(request):
    messages = MessageRecipient.objects.filter(recipient=request.user, is_read=False)
    context = {
        'messages': messages
    }
    return render(request, 'home.html', context)


def inbox(request):
    return render(request, 'inbox.html')

def feedback(request):
    return render(request, 'feedback.html')

def profile(request):
    return render(request, 'profile.html')

def settings(request):
    return render(request, 'settings.html')

def call(request):
    return render(request, 'calls.html')


def kall(request):
    return render(request, 'kall.html')



def register(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        username = request.POST["username"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        password1= request.POST["password1"]
        password2 = request.POST["password2"]
        if password1 == password2: 
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Already exists")
            elif User.objects.filter(email=email).exists():
               messages.info(request, "Email Already exists")
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name= last_name)
                user.save();
                
        else:
            messages.info(request, "PAssword didnt match ")
        return redirect('home')


    else:
        return render(request, 'register.html')
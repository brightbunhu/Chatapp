from django.shortcuts import render, redirect
from .models import Message, MessageRecipient
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.shortcuts import get_object_or_404

from.forms import SendMessageForm

@login_required(login_url='/register/')
def home(request, pk):
    user = User.objects.get(pk=pk)
    messages = MessageRecipient.objects.filter(recipient=user, is_read=False)
    context = {
        'messages': messages
    }
    return render(request, 'home.html', context)

@login_required(login_url='/register/')
def inbox(request, pk):
    user = User.objects.get(pk=pk)
    messages = MessageRecipient.objects.filter(recipient=user, is_read=False)
    sent_messages = Message.objects.filter(sender=user)  # Assuming you have a Message model
    default_recipient = User.objects.first().pk  # or some other default recipient
    context = {
        'messages': messages,
        'sent_messages': sent_messages,
        'users': User.objects.all(),
        'default_recipient': default_recipient
    }
    return render(request, 'inbox.html', context)
@login_required(login_url='/register/')
def send_message(request, recipient_id):
    recipient = get_object_or_404(User, id=recipient_id)
    if request.method == 'POST':
        form = SendMessageForm(request.POST)
        if form.is_valid():
            message = Message(content=form.cleaned_data['content'], sender=request.user)
            message.save()
            message_recipient = MessageRecipient(message=message, recipient=recipient)
            message_recipient.save()
            return redirect('inbox', pk=request.user.id)
    else:
        form = SendMessageForm()
    return render(request, 'send_message.html', {'form': form, 'recipient': recipient})
@login_required(login_url='/register/')
def mark_as_read(request, pk):
    message = MessageRecipient.objects.get(pk=pk)
    message.is_read = True
    message.save()
    return redirect('inbox', pk=request.user.pk)




























@login_required(login_url='/register/')
def feedback(request):
    return render(request, 'feedback.html')


@login_required(login_url='/register/')
def profile(request, pk):
    user = User.objects.get(pk=pk)
    return render(request, 'profile.html', {'user': user})
    

@login_required(login_url='/register/')
def settings(request):
    return render(request, 'settings.html')
@login_required(login_url='/register/')
def call(request, pk):
    return render(request, 'calls.html')

@login_required(login_url='/register/')
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
        return redirect('login')


    else:
        return render(request, 'register.html')
    

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home', user.id)
        else:
            messages.info(request, "Invalid Credentials")
            return redirect('login')
    else:
        return render(request, 'login.html')
    



def logout(request):
    auth.logout(request)
    return redirect('/')
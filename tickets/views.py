from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from .models import RaiseTicketForm
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
  
  

def index(request):
    return render(request, 'user/index.html', {'title':'Ticket Manager'})



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            ######################### mail system ##############################
            htmly = get_template('user/Email.html')
            d = { 'username': username }
            subject, from_email, to = 'Welcome', 'your_email@gmail.com', email
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            ##################################################################
            messages.success(request, f'Your account has been created, you may now log in!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form, 'title':'Signing up'})
  


def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' Welcome {username} !!')
            return redirect('index')
        else:
            messages.info(request, f'Wrong info, try again or sign up!')
    form = AuthenticationForm()
    return render(request, 'user/login.html', {'form':form, 'title':'Log In'})



def Logout(request):
    logout(request)
    return render(request, 'user/index.html', {'title':'Ticket Manager'})



def All_tickets_view(request):
    context = RaiseTicketForm.objects.all()
    return render(request, 'user/status.html', {'context':context,'title':'All tickets'})



def Raise_ticket(request):
    if request.method == 'POST':
        ticket = models.RaiseTicketForm.objects.create(
            subject = request.POST['subject'],
            issue = request.POST['issue']
        )
        ticket.save()
        messages.success(request, f'Your valuable feedback was heard!')
        return redirect('status')
    else:
        ticket = RaiseTicketForm()
    return render(request, 'user/status.html', {'context': ticket, 'title':'New ticket'})
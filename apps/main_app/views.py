from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt

def index(request):
    return render(request, "main_app/index.html")

def login_reg_page(request):
    if "logged_in" in request.session:
        return redirect('/donation')
    return render(request, "main_app/login_reg.html")

def register_user(request):
    errors = User.objects.register_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags = key)
        return redirect('/login_reg_page')
    hashpw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
    user = User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = hashpw)
    request.session['logged_in'] = True
    request.session['user_id'] = user.id
    return redirect('/')

def login_user(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags = key)
        return redirect('/login_reg_page')
    user = User.objects.filter(email = request.POST['email'])
    request.session['logged_in'] = True
    request.session['user_id'] = user[0].id
    return redirect('/')

def help_suicide(request):
    return render(request, "main_app/suicide.html")

def help_homeless(request):
    return render(request, "main_app/homeless.html")

def help_disability(request):
    return render(request, "main_app/disability.html")

def help_social(request):
    return render(request, "main_app/social.html")

def help_violence(request):
    return render(request, "main_app/violence.html")

def log_out(request):
    del request.session['user_id']
    del request.session['logged_in']
    return redirect('/login_reg_page')

def donation(request):
    return render(request, "main_app/donation.html")

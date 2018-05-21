from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *

def index(request):
    if 'id' in request.session:
        return redirect('/success')
    return render(request, 'login_reg_flow/index.html')
def register(request):
    if request.method == 'POST':
        errors = User.objects.basic_validator(request.session, request.POST)
        if len(errors) == 0:
            if User.objects.register_new_user(request.session, request.POST):
                return redirect('/success')
            else:
                print("==============Unable to register user==============")
                return redirect('/')
        else:
            print("Found " + str(len(errors)) + " errors!")
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
    else:
        return redirect('/')
def login(request):
    if request.method == 'POST':
        user = User.objects.validate_login(request.session, request.POST)
        if user:
            return redirect('/success')
        else:
            messages.error(request, "The email and password provided do not match any records in our database")
            return redirect('/')
    else:
        return redirect('/')
def success(request):
    if 'id' in request.session:
        name = User.objects.get(id=request.session['id']).first_name
        return render(request, 'login_reg_flow/success.html', {'name':name})
    else:
        messages.error(request, "You must be logged in to view that page.") 
        return redirect('/')
def logout(request):
    if 'id' in request.session:
        request.session.pop('id')
    return redirect('/')
from django.shortcuts import render, redirect
from . import register
from django.contrib.auth import login
from django.conf import settings

# Create your views here.
def Register(request):
    form = register.SignupForm()
    if request.method == "POST":
        form = register.SignupForm(request.POST)
        if form.is_valid:
           user =  form.save()
           login(request, user)
           return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'register.html', {"form", "hello"})
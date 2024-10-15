from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login as login_user
from .models import User
from django.contrib.auth.decorators import login_required
import datetime

def to_login(request):
    return redirect(reverse('login'))

def login(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect(reverse('plataforma'))
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)
        if user:
            login_user(request, user)
            return JsonResponse({'code': '200'})
        else:
            return JsonResponse({'code': '401', 'redirectURL': reverse('login')})

def logout(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            request.session.flush()
            return redirect(reverse('login'))
        else:
            return redirect(reverse('login'))

@login_required()     
def plataforma(request):
    if request.method == 'GET':
        user = get_object_or_404(User, username=request.user.username)
        return render(request, 'plataforma.html', {'sistemas': user.sistemas.all()})

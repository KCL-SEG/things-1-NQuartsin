from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect, render

def home(request):
    return render(request, 'home.html')

from django.core.paginator import Paginator
from django.shortcuts import render,redirect
from django.contrib.auth import User
from bson import ObjectId
from ..models import *

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User
    return render(request, 'auth/login.html')
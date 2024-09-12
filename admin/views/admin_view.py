from django.shortcuts import render
from django.contrib.auth import login, authenticate
def dashboard(request):
    user = authenticate(request, username='admin', password='123123')
    if user is not None:
        login(request, user)
    print(request.user.id)
        
    return render(request, 'dashboard.html')
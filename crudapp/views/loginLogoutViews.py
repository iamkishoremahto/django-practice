from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout


def login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)
        

        if user is not None:
            print(user)
            auth_login(request,user)
            return redirect('home')
        else:
            return render(request, 'login.html', {"error": "Invalid username or password "})


    return render(request, 'pages/login.html')

def logout(request):
    auth_logout(request)
    return redirect('home')
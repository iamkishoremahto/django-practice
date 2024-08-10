
from django.shortcuts import render, redirect

def checkLogin(request,func):
    def wrapper_func(request,*args, **kwargs):
        if not request.user.is_authenticated:
            redirect('login')
        return func(request, *args, **kwargs)
    return wrapper_func

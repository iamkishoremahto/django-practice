from django.shortcuts import render,redirect
from .. import models, encoding
from django.contrib.auth.decorators import login_required

# Create your views here.

def checkLogin(func):
    def wrapper_func(request,*args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return func(request, *args, **kwargs)
    return wrapper_func



@checkLogin
def home(request):

    students = models.Student.objects.all()
  
    
    return render(request, 'pages/home.html', {"students": students,"username": request.user.username})

@checkLogin
def addStudent(request):
    if request.method == 'POST':
        form = {key:value for key, value in request.POST.items() if key != "csrfmiddlewaretoken"}
        # form.pop('csrfmiddlewaretoken')
        newStudent = models.Student.objects.create(**form)
        newStudent.save()
        return redirect('home')

@checkLogin
def updateStudent(request,pk):
  

    if request.method == 'POST':
        
        form = {key:value for key, value in request.POST.items() if key != "csrfmiddlewaretoken"}

        student = models.Student.objects.filter(id= pk)
        student.update(**form)
        return redirect('home')
        
    student = models.Student.objects.get(pk=pk)
    return render(request, 'pages/updateStudent.html', {"student":student})

@checkLogin   
def deleteStudent(request,pk):
 

    student = models.Student.objects.get(pk=pk)
    student.delete()
    return redirect('home')



from django.contrib import messages, auth
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import User, Admin_User
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
import datetime
from django.contrib.auth import login as auth_login

# Create your views here.
def home(request):
    # return HttpResponse('This is home')

    allUsers = User.objects.all().order_by('-user_id')
    context = {"allUsersdata": allUsers}
    return render(request, 'front/index.html', context)


def login(request):
    # return HttpResponse('This is home')
    return render(request, 'front/login.html')


def handleLogin(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        admin_user = auth.authenticate(username=email, password=password)

        if admin_user is not None:
            login(request, admin_user)
            messages.success(request, "Login success")
            messages.error(request, "Email name password worng !!")
            # return redirect('/')

        else:
            return redirect('/')
            # messages.error(request, "Email name password worng !!")


    return HttpResponse('404 - Not Found')


def handelRegister(request):
    if request.method == "POST":
        admin_name = request.POST['admin_name']
        email = request.POST['email']
        password = request.POST['password']

        # Check for error inputs

        userdata = Admin_User(admin_name=admin_name, email=email, password=password)
        userdata.save()
        messages.success(request, "Your Account has been successfully created !!")
        return render(request, 'front/login.html')


def register(request):
    # return HttpResponse('This is home')
    return render(request, 'front/register.html')


def table(request):
    # return HttpResponse('This is home')
    return render(request, 'front/tables.html')


def addnew(request):
    return render(request, 'front/add_member.html')


def addnewdata(request):
    if request.method == "POST":
        name = request.POST['name']
        image = request.POST['image']
        date = request.POST['date']
        time = request.POST['time']
        position = request.POST['position']

        # Check for error inputs

        userdata = User(name=name, image=image, date=date, time=time, position=position)
        userdata.save()
        messages.success(request, "Your Account has been successfully created !!")
        return redirect('/')

    else:
        return HttpResponse('404 - Not Found')


def deletedata(request, user_id):
    pi = User.objects.get(user_id=user_id)
    pi.delete()
    return HttpResponseRedirect('/')


def edituser(request, user_id):
    # return HttpResponse('This is home')
    gdata = User.objects.get(user_id=user_id)
    return render(request, 'front/edituser.html', {"gdata": gdata})


def updatedata(request, user_id):
    if request.method == 'POST':
        student_obj = User.objects.get(user_id=user_id)
        student_obj.name = request.POST['name']
        student_obj.image = request.POST['image']
        student_obj.date = request.POST['date']
        student_obj.time = request.POST['time']
        student_obj.position = request.POST['position']
        student_obj.save()
        return redirect('/')

from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate,logout
# Create your views here.
def indexView(request):
    return render(request,"index.html")

def register(request):
    if(request.method=="POST"):
        fname=request.POST.get("fname")
        lname=request.POST.get("lname")
        email=request.POST.get("email")
        username=request.POST.get("username")
        password=request.POST.get("password")
        print(fname,lname,email,username,password)
        user = User(username=username, first_name=fname, last_name=lname, email=email)
        user.set_password(password)  # Hash the password securely
        user.save()
        return redirect("/")
    return render(request,"register.html")

def loginUser(request):
    if(request.method=="POST"):
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(username=username,password=password)
        if(user is not None):
            login(request,user)
            return redirect("/home")
        else:
            return redirect("/accounts/login/")
    return render(request,"login.html")

def logoutUser(request):
    logout(request)
    return redirect("/accounts/login/")


@login_required
def home(request):
    return render(request,"home.html")


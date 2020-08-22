from django.contrib.auth import authenticate
from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from django.contrib import messages
from django.contrib.auth import logout,login
from django.contrib.auth.models import User

from userde.models import Contact

# Create your views here.
def home(req):
    if req.user.is_anonymous:
        return redirect("/login")
    return render(req, "main.html")







def contact(req):
    if req.method=="POST":
        name=req.POST.get('name')
        email = req.POST.get('email')
        desc = req.POST.get('desc')
        contact=Contact(name=name,email=email,desc=desc,date=datetime.today())
        contact.save()
        messages.success(req, 'Your Contact avs been send')


    return render(req,"contact.html")


def loginUser(req):
    if req.method == "POST":
        username = req.POST.get('uname')
        password = req.POST.get('pass')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(req,user)
            return redirect("/")


    else:
        return render(req, "login.html")

    return render(req,"login.html")


def logoutUser(req):

    logout(req)

    return redirect("/login")




def signupUser(req):

    if req.method=="POST":
        uname=req.POST.get('uname')
        fname = req.POST.get('fname')
        lname= req.POST.get('lname')
        email= req.POST.get('email')
        pn= req.POST.get('pn')
        passw= req.POST.get('passw')
        cpass= req.POST.get('cpass')
        myuser=User.objects.create_user(uname,email,passw)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(req, 'Your Account Registerd Suceesfully ...')
        return redirect("/")
    else:
        return render(req,"Signup.html")

















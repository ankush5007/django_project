from django.contrib.auth import authenticate, login
from django.shortcuts import render,redirect
from django.http import  HttpResponse
from django.http import  HttpRequest
from django.contrib.auth.models import User,auth
from django.contrib import  messages
from .models import  Destination ## load model or load view ,
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def indexPageview(request):
    data = Destination.objects.all()
    output = {"dests":data}
    #output =dest1.__dict__ ## convert to dict
    return render(request,'index.html',output)

def registerPageview(request):
    if request.method == "POST":
        f_name = request.POST["first_name"]
        l_name = request.POST["last_name"]
        u_name = request.POST["user_name"]
        email  = request.POST["email"]
        pass_1 = request.POST["password1"]
        pass_2 = request.POST["password2"]
        is_admin = request.POST["is_admin"]

        ## can run map tp entire object to check any field is empty

        if (pass_1 != pass_2):
            messages.info(request,"password does not match")
            return redirect("register")
        else:
            if not(User.objects.filter(username=u_name).exists() or User.objects.filter(email = email).exists()):
                user = User.objects.create_user(username=u_name, first_name=f_name, last_name=l_name, email=email,
                                              password = pass_1  , is_superuser=bool(is_admin),is_staff = bool(is_admin))
                user.save()
                messages.info(request,"user created!")
                return redirect("login")
            else:
                messages.info(request,"user already exists")
                return redirect("register")
    else:
        return render(request,'register.html')




def manage_authPageview(request):
    if request.method == "POST":
        username = request.POST['user_name']
        password = request.POST['password']
        print (username)
        print(password)
        print (len(password))
        user1 = auth.authenticate(user_name = username, password= password)
        print (user1)
        if user1 is not None:
            auth.login(request,user1)
            return redirect("/")
        else:
            messages.info(request,"invalid crediantls")
            return redirect("login")

    else:
        return render(request,'login.html')


def logoutPageview(request):
    auth.logout(request)
    return redirect('/')

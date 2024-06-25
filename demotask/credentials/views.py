from django.contrib import messages, auth
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
# Create your views here.

def login(request):
    if request.method=="POST":
        user_name=request.POST['username']
        pass_word=request.POST['password']
        user=auth.authenticate(username=user_name,password=pass_word)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid credentials")
            return redirect('login')
    return render(request,"login.html")

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        firstname=request.POST['first_name']
        lastname=request.POST['last_name']
        email_id=request.POST['email']
        password=request.POST['password']
        confirmpassword=request.POST['password1']
        if password==confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already exists")
                return redirect('register')
            elif User.objects.filter(email=email_id).exists():
                messages.info(request,"email already exists")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,password=password,email=email_id)
                user.save()
                return redirect('login')
                print("User Created")
        else:
            messages.info(request,"Password not matched")
            #print ("Password not matched ")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')
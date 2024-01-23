from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect

from bank.forms import ApplicationForm


# Create your views here.
def home(request):
    return render(request,'index.html')

def apply(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bankapp:success')
    else:
        form = ApplicationForm()
    return render(request, 'application_form.html', {'form': form})

def success(request):
    return render(request, 'success.html')
def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid credentials")
            return redirect('bankapp:login')
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username taken")
                return redirect('bankapp:register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email taken")
                return redirect('bankapp:register')
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                user.save();
                print("User created")
                return redirect('bankapp:login')

        else:
            messages.info(request,"Password Not match")
            return redirect('bankapp:register')
    return render(request, 'register.html')
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import RegistrationForm


# Create your views here.
def home(request):
    return render(request,'index.html')

def show_application_form(request):
    return render(request, 'application_form.html')

def submit_application(request):
    # Add form submission logic here
    message = "Application accepted"
    return render(request, 'application_form.html', {'message': message})
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
        form = RegistrationForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            cpassword = form.cleaned_data['password1']

            if password == cpassword:
                if User.objects.filter(username=username).exists():
                    messages.error(request, "Username taken")
                    return redirect('bankapp:register')
                elif User.objects.filter(email=email).exists():
                    messages.error(request, "Email taken")
                    return redirect('bankapp:register')
                else:
                    user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
                    user.save()
                    print("User created")
                    return redirect('bankapp:login')
            else:
                messages.error(request, "Passwords do not match")
                return redirect('bankapp:register')
        else:
            messages.error(request, "Please fill out the form correctly")
            return render(request, 'register.html', {'form': form})
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})

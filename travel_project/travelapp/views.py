from django.http import HttpResponse
from django.shortcuts import render
from . models import Blog_Rent,Team


# Create your views here.
def home(request):
    obj = Blog_Rent.objects.all()
    obj1 = Team.objects.all()
    return render(request,'index.html',{'result':obj,'result1':obj1})
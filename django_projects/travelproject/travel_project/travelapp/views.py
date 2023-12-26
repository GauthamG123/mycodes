from django.http import HttpResponse
from django.shortcuts import render
from . models import Blog_Rent


# Create your views here.
def demo(request):
    obj = Blog_Rent.objects.all()
    return render(request,'index.html',{'result':obj})
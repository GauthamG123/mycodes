from django.shortcuts import render, redirect
import requests
from bs4 import BeautifulSoup

from . models import Links


# Create your views here.
def home(request):
    if request.method=='POST':
        new_link = request.POST.get('page','')
        urls=requests.get(new_link)
        bs = BeautifulSoup(urls.text,'html.parser')
        for link in bs.find_all('a'):
            li_address = link.get('href')
            li_name = link.string
            Links.objects.create(address=li_address,stringname=li_name)
        return redirect('/')
    else:
        data_values = Links.objects.all()
    return render(request,'home.html',{'data_value':data_values})
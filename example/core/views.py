

# Create your views here.
from django.shortcuts import render
from core.models import Contact
from datetime import datetime
from django.db import models
from django.shortcuts import render,HttpResponse

# Create your views here.

def contact(request):
   
    return render(request,'contactus.html')

def q(request):                                                                    
       
    return render(request,'swiper.html')

def index(request):
    if request.method =='POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact=Contact(fname=fname,lname=lname,email=email,phone=phone,message=message)
        contact.save()
    return render(request,'index.html')
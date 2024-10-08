from django.shortcuts import render
from django.http import HttpResponse
from .models import application
# Create your views here.
def home(request):
    return render(request,"home.html")
def register(request):
    fname=request.POST['firstname']
    lname=request.POST['lastname']
    password=request.POST['password']
    address=request.POST['address']
 
    application.objects.create(First_Name=fname, password=password)
    
    return render(request,"result.html",{'fname':fname,'lname':lname,'password':password,'address':address})
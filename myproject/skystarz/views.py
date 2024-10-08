from django.shortcuts import render
from django.http import HttpResponse
from models import star
# Create your views here.
def index(request):
    return render(request,"index.html")

def register(request):
    username=request.POST["username"]
    email=request.POST["email"]
    password=request.POST["password"]
    star.objects.create(user_name=username,emai_l=email,pass_word=password)
    return render(request,"reg.html",{})
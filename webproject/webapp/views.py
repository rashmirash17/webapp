
from django.shortcuts import render
from django.http import HttpResponse

user_list = []

def home(request):
    return render(request,'home.html')

def register(request):  
    return render(request,'adduser.html')

def register2(request):
    return render(request,'adduser2.html')

def adduser(request):
    id=request.GET.get('id')
    name=request.GET.get('name')
    email=request.GET.get('email')
    contact=request.GET.get('contact')
    t=(id,name,email,contact)
    return HttpResponse(str(t))

def adduser2(request):
    id=request.POST.get('id')
    name=request.POST.get('name')
    email=request.POST.get('email')
    contact=request.POST.get('contact')
    t=(id,name,email,contact)
    user_list.append(t)
    return render(request,'home.html')

def ulist(request):
    return render(request,'ulist.html',{'l':user_list})
# Create your views here.

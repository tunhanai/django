from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import *
import json
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here. 
def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username= request.POST.get('username')
        password= request.POST.get('password')
        user= authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:messages.info(request,'user or password not correct!')
    context = {}
    # Xử lý yêu cầu đăng nhập
    return render(request,'app/login.html',context)
def logoutpage(request):
    logout(request)
    return redirect('login')
def register(request):
    # Xử lý yêu cầu đăng ki
    form = Taotk()
   
    if request.method == "POST":
        form =Taotk(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request,'app/register.html',context)
def home(request):
    phongs= Phong.objects.all()
    context={'phongs':phongs}
    return render(request,'app/home.html',context)
def cart(request):
    if request.user.is_authenticated:
        nguoidung= request.user.nguoidung
        datphong, created= Datphong.objects.get_or_create(nguoidung =nguoidung, complete = False)
        items=datphong.dsdat_set.all()
    else:
        items = []
        datphong = {'get_cart_items':0, 'get_cart_tong':0}
    context={'items':items,'datphong':datphong}
    return render(request,'app/cart.html',context) 
def checkout(request):
    if request.user.is_authenticated:
        nguoidung= request.user.nguoidung
        datphong, created= Datphong.objects.get_or_create(nguoidung =nguoidung, complete = False)
        items=datphong.dsdat_set.all()
    else:
        items = []
        datphong = {'get_cart_items':0, 'get_cart_tong':0}
    context={'items':items,'datphong':datphong}
    return render(request,'app/checkout.html',context)
    
def updateItem(request):
    data = json.loads(request.body)
    idphong=data['idphong']
    action=data['action']
    nguoidung=request.user.nguoidung
    phong = Phong.objects.get(id=idphong)
    datphong, created= Datphong.objects.get_or_create(nguoidung =nguoidung, complete = False)
    Dsdat, created= dsdat.objects.get_or_create(datphong =datphong, phong = phong)
    if action=='add':
        Dsdat.sl +=1
    elif action =='remove':
        Dsdat.sl -=1
    Dsdat.save()
    if Dsdat.sl<=0: 
        Dsdat.delete() 
    return JsonResponse('added',safe=False)




from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Product
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login,logout,authenticate
from .forms import addproductform


# Create your views here.

def home(request):
    return render (request,'bill/home.html')

def productlists(request):

    productlist = Product.objects.all()
    return render (request,'bill/productdetails.html',{'productlist':productlist})

def signupuser(request):
    if request.method == 'GET':
        return render(request,'bill/signupuser.html',{'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('currentview')
            except IntegrityError:
                return render (request,'bill/signupuser.html',{'form':UserCreationForm(), 'error':'UserName already taken'})
        else:
            return render(request,'bill/signupuser.html',{'form':UserCreationForm(), 'error':'Passwords didnot match'})

def loginuser(request):
    if request.method == 'GET':
        return render(request,'bill/loginuser.html',{'form':AuthenticationForm()})
    else:
        user = authenticate(request,username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request,'bill/loginuser.html',{'form':AuthenticationForm(),'error':'UserName and password did not match'})
        else:
            login(request,user)
            return redirect('currentview')

def logoutuser(request):
    if request.method=='POST':
        logout(request)
        return redirect ('home')

def currentview(request):
    productlist = Product.objects.all()
    return render(request,'bill/currentview.html',{'productlist':productlist})

def addproduct(request):
    if request.method == 'GET':
        return render(request,'bill/addproduct.html',{'form':addproductform()})
    else:
        form = addproductform(request.POST)
        form.save()
        return redirect('currentview')

def viewproduct(request,product_pk):
    product = get_object_or_404(Product,pk=product_pk)
    if request.method == 'GET':
        form = addproductform(instance=product)
        return render(request,'bill/viewproduct.html',{'product':product,'form':form})
    else:
        try:
            form = addproductform(request.POST,instance=product)
            form.save()
            return redirect('currentview')
        except ValueError:
            return render(request,'bill/viewproduct.html',{'product':product,'form':form,'error':badinfo})

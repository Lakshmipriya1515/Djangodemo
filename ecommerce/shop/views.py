from django.shortcuts import render,redirect
from shop.models import Category,Product
from django.http import HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def allcategories(request):
    t=Category.objects.all()
    return render(request,'category.html',{'t':t})
def product(request,p):
    t=Category.objects.get(name=p)
    p=Product.objects.filter(category=t)
    return render(request,'product.html',{'t':t,'p':p})
def detail(request,p):
    p = Product.objects.get(name=p)
    return render(request, 'detail.html', { 'p': p})



def register(request):
    if(request.method=="POST"):
        n = request.POST['n']
        p = request.POST['p']
        t = request.POST['t']
        e = request.POST['e']
        f=request.POST['f']
        l=request.POST['l']
        pl=request.POST['pl']
        h=request.POST['h']
        if(p==t):
            user = User.objects.create_user(username=n,password=p,email=e,first_name=f,last_name=l)
            user.save()
            return render(request,'category.html')
        else:
            return HttpResponse("passwords are not same")

    return render(request,'register.html')

def user_login(request):
    if(request.method=="POST"):
        n=request.POST['n']
        p=request.POST['p']
        user=authenticate(username=n,password=p)
        if user:
            login(request,user)
            return redirect('shop:allcat')
        else:
            return HttpResponse("Invalid credentials")
    return render(request,'login.html')
@login_required
def user_logout(request):
    logout(request)
    return redirect('shop:user_login')


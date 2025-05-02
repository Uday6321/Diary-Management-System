from webbrowser import register

from django.http import HttpResponse
from django.shortcuts import render,redirect
from pymsgbox import password
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from .models import *
from django.contrib.auth.models import User,auth
# Create your views here.
def home(request):
    obj=Demo()
    obj.name="Mango"
    obj.price=10
    obj.yn=True
    obj1=Demo()
    obj1.name="Apple"
    obj1.price=100
    obj1.yn=False
    #lis=[obj,obj1]
    lis=Demo.objects.all()
    a='Strawberry'
    b=9
    return render(request,"home.html",{'list':lis})
def add_template(request):
    return render(request,'additionof2.html')

def addition(request):
    n1=request.POST['a']
    n2=request.POST['b']
    c=int(n1)+int(n2)
    return render(request,'additionof2.html',{'sum':c})
def register_template(request):
    if request.method=='POST':
        user=request.POST['username']
        ema=request.POST['email']
        pas=request.POST['password']
        add="Sorry "+user+" username already exists please try with another username..."
        if User.objects.filter(username=user).exists():
            return render(request,'Register.html',{'me':add})
        else:
            us=User.objects.create_user(username=user,email=ema,password=pas)
            us.save()
            return redirect('/login')
    else:
        return render(request,'Register.html')
@csrf_exempt
def login(request):
    if request.method=='POST':
        user = request.POST['username']
        pas = request.POST['password']
        us=auth.authenticate(username=user,password=pas)
        if us is not None:
            auth.login(request,us)
            return render(request,'Success.html',{'me':user})
            #return redirect('/success')
        else:
            mes='Hey '+user+' invalid credentials please try again...'
            return render(request,'Login.html',{'me':mes})
    else:
        return render(request,'Login.html')
def success(request):
    return render(request,'Success.html')
def record(request):
    if request.method=='POST':
        usernam=request.POST['username']
        dat=request.POST['date']
        tex=request.POST.get('text')
        u=Record(username=usernam,date=dat,text=tex)
        u.save()
        sd="Data submitted successfully..."
        return render(request,'record.html',{"ss":sd})
    else:
        return render(request,'record.html')
def recorddata(request):
    if request.method=='POST':
        usern=request.POST['username']
        liss=Record.objects.filter(username=usern).first()
        sas="username not found..."
        listt=Record.objects.all();
        if liss:
            return render(request, 'data.html', {'list': listt,'name' :liss.username})
        else:
            return render(request,'data.html',{'sss':sas})
    else:
        return render(request,'recorddata.html')

def sample(request):
    if request.method=='POST':
       t1=request.POST['text1']
       t2=request.POST['text2']
       z=Samp(text1=t1,text2=t2)
       z.save()
       return redirect('/samp')
    else:
        return render(request,'samp.html')
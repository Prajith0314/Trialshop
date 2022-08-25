from http.client import HTTPResponse
from urllib import response
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth

a="Php"
m="testing"

def index(request):
   return render(request,"index.html")

def samp(request):
   return render(request,"test.html",{'l':a,'P':m})

def login1(request):
   return render(request,"login.html")

def register(request):
   return render(request,"register.html")
  
   #user=auth.authenticate(username=username,Firstname=Firstname,Lastname=Lastname,Email=Email,Password=Password,RePassword=RePassword)
   
def logincheck(request):
   name=request.GET["newline"]
   password=request.GET['line']
   user=auth.authenticate(username=name,password=password)
   if user is not None:
      auth.login(request,user)
      return redirect("/")
   else:
        return redirect("/login1")

def registercheck(request):
   username=request.GET['Username']
   Firstname=request.GET['Firstname']
   Lastname=request.GET['Lastname']
   Email=request.GET['Email']
   Password=request.GET['Password']
   RePassword=request.GET['RePassword']
   uchk=User.objects.filter(username=username)
   echk=User.objects.filter(email=Email)
   print(uchk)

   if uchk:
      na="username is already taken"
      return render(request,"test.html",{'key3':na})
   elif echk:
      na="email is already taken"
      return render(request,"test.html",{'key3':na})
   elif Password!=RePassword:
      na="Password is invalid"
      return render(request,"test.html",{'key3':na})
   else:
      user=User.objects.create_user(username=username,first_name=Firstname,last_name=Lastname,email=Email,password=Password)
      user.save();
      return redirect('/')

   return render(request,"test.html",{'key3':na,'key4':Firstname,'key5':Lastname,'key6':Email,'key7':Password,'key8':RePassword})
        



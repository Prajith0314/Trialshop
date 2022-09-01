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
   if request.method=='POST':
      name=request.POST["newline"]
      password=request.POST['line']
      user=auth.authenticate(username=name,password=password)
      if user is not None:
         auth.login(request,user)
         return redirect("/")
      else:
         msg="invalid username and password"
         return render(request,"login.html",{'msg':msg})
   else:
      return render(request,"login.html")

def register(request):
   if request.method=='POST':
      username=request.POST['Username']
      Firstname=request.POST['Firstname']
      Lastname=request.POST['Lastname']
      Email=request.POST['Email']
      Password=request.POST['Password']
      RePassword=request.POST['RePassword']
      uchk=User.objects.filter(username=username)
      echk=User.objects.filter(email=Email)



      
      if uchk:
         na="username is already taken"
         return render(request,"register.html",{'msg':na})
      elif echk:
         na="email is already taken"
         return render(request,"register.html",{'msg':na})
      elif Password!=RePassword:
         na="Password is invalid"
         return render(request,"register.html",{'msg':na})
      else:
         user=User.objects.create_user(username=username,first_name=Firstname,last_name=Lastname,email=Email,password=Password)
         user.save();
         auth.login(request,user)

         return redirect('/')
      
   else:
      return render(request,"register.html")
def logout(request):
   auth.logout(request)
   return redirect("/")
def product(request):
   return render(request,"test.html")         
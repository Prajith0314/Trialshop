from math import fabs
from unicodedata import name
from winreg import FlushKey
from django.shortcuts import render,redirect
from .models import fashion_collection,comment_box
from django.http.response import JsonResponse

def about(request):
   if request.method=='POST':
      pro_name=request.POST['search']
      pro=fashion_collection.objects.get(name=pro_name)
   else:
      id=request.GET['id']
      pro=fashion_collection.objects.get(id=id)
   return render(request,'about.html',{'key1':pro})

def comment(request):
   name=request.POST['user']
   message=request.POST['msg']
   product=request.POST['pro']
   cmt=comment_box.objects.create(name=name,msg=message,fkey_id=product)
   cmt.save();
   return redirect('/')

def review(request):
   if 'term' in request.GET:
      name=request.GET['term']
      pro=fashion_collection.objects.filter(name__istartswith=name)
      print(pro)
      e=[]
      for i in pro:
         e.append(i.name)
      print(e)
      return JsonResponse(e,safe=False)
   return render(request,"test.html")   


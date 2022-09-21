from unicodedata import name
from winreg import FlushKey
from django.shortcuts import render,redirect
from .models import fashion_collection,comment_box

def about(request):
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


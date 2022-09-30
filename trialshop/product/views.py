
from django.shortcuts import render,redirect
from .models import fashion_collection,comment_box
from django.http.response import JsonResponse
from django.core.cache import cache

def about(request):
   id=request.GET['id']
   if cache.get(id):
      pro=cache.get(id)
      print('DATA FROM CACHE')
   else:
      pro=fashion_collection.objects.get(id=id)
      cache.set(id,pro)
      print('DATA FROM DATABASES')
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


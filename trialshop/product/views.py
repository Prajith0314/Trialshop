from django.shortcuts import render
from .models import fashion_collection

def about(request):
   id=request.GET['id']
   pro=fashion_collection.objects.get(id=id)
   print(pro)
   return render(request,'about.html',{'key1':pro}) 

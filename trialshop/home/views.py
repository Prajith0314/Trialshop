from http.client import HTTPResponse
from urllib import response
from django.shortcuts import render

def index(request):
   return render(request,"test.html")


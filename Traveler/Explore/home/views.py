from django.shortcuts import render
def index(request):
        return render(request,'test.html')
def samp(request):
        return render(request,"index.html")
def login(request):
        return render(request,"Login1.html")                
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.about2,name="about"),
    path('cmt/',views.comment,name="review"),
    path('srh/',views.review,name="comments"),
    
]
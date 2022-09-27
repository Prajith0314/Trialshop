from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.about,name="about"),
    path('cmt/',views.comment,name="review"),
    path('srh/',views.review,name="comments"),
    
]
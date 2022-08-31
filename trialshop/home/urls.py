from django.urls import path
from.import views

urlpatterns = [
    path('',views.index,name="home"),
    path('samp/',views.samp,name="project"),
    path('login1/',views.login1,name="login"),
    path('register/',views.register,name="register"),
    path('logout/',views.logout,name="logout"),
  
]
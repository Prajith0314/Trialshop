from django.urls import path
from.import views
from.feed import latest_feed

urlpatterns = [
    path('',views.index,name="home"),
    path('samp/',views.samp,name="comment_entry"),
    path('login1/',views.login1,name="login"),
    path('register/',views.register,name="register"),
    path('logout/',views.logout,name="logout"),
    path('feed/',latest_feed()),
    
  
]
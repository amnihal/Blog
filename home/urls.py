from django.urls import path
from.import views



urlpatterns = [
    path('',views.home,name="home"),
    path('content/<str:id>',views.content,name="content"),
    path('signup',views.signup,name="signup"),
    path('login',views.Log_in,name="login"),
    path('logout',views.Log_out,name="logout"),
]

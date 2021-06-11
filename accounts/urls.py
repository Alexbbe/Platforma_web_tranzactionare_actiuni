from django.contrib import admin
from django.urls import path
from accounts import views
urlpatterns = [

    path('userlogin', views.UserLogin, name='userlogin'),
    path('register', views.register, name='register'),
    path('complete_account',views.complete_user, name='complete_user'),
    path('logout',views.logoutUser,name='logoutUser')

]

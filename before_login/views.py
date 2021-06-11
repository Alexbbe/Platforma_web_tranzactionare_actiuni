from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,'before_login/home.html')
from django.shortcuts import render,redirect
from django.http import HttpResponse
from accounts.forms import RegisterForm, User_complete
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from accounts.models import MyUser

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for new user:' + user)
            return redirect('userlogin')
    else:
        form = RegisterForm()

    context = {'form': form}
    return render(request,'accounts/register.html',context)


def UserLogin(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(email = email, password = password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, "Username or password is incorrect")

    return render(request, 'accounts/login.html')


def logoutUser(request):
    logout(request)
    return redirect('home')

def complete_user(request):
    if request.method == 'POST':
        form = User_complete(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = User_complete()


    return render(request, 'accounts/complete_account.html', {'form': form,'search_list':list1})


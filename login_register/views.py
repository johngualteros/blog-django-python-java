from django.shortcuts import render,redirect
from .models import User
# Create your views here.
def register(request):
    return render(request, 'register.html')
def create_user(request):
    user = User(userName=request.POST.get('user'),password=request.POST.get('password'))
    user.save()
    print(request.POST)
    return redirect('/foreach/')
def login(request):
    return render(request, 'login.html')
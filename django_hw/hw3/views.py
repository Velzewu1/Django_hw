from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')

def login_view(request):
    return render(request, 'main/login.html')
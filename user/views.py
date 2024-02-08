from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, logout
from user.authentication import TestAuthentication

from user.forms import RegisterUserForm

class RegisterView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('dashboard')
        else:
            return render(request, 'register.html',{'form':RegisterUserForm()})

    def post(self, request):
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            form.save()
            user = TestAuthentication.authenticate(request, email=email, password=password)
            login(request, user)
            return redirect('dashboard')
        else:
            return redirect('register')

class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('dashboard')
        else:
            return render(request, 'login.html')

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        user = TestAuthentication.authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return redirect('login')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')
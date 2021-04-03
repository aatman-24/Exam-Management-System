from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import AuthenticationForm

class LoginView(auth_views.LoginView):
    template_name = 'user/login.html'

class LogoutView(auth_views.LogoutView):

    template_name = 'user/logout.html'
    extra_context = {'form' : AuthenticationForm}

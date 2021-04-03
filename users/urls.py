from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import  RedirectView
from .views import LoginView, LogoutView

app_name = 'user'

urlpatterns = [
    path('',RedirectView.as_view(pattern_name='dj-auth:login', permanent = False)),
    path('login/',LoginView.as_view(),name="login"),
    path('logout/',LogoutView.as_view(),name="logout"),
]

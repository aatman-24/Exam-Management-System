from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import  RedirectView, TemplateView
from .views import LoginView, LogoutView, PasswordChangeDoneView, PasswordChangeView, \
                    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView, \
                    DisableAccount, ActivateAccount, CreateAccount, ResendActivationEmail

app_name = 'users'

urlpatterns = [
    path('',RedirectView.as_view(pattern_name='dj-auth:login', permanent = False)),

    path('login/',LoginView.as_view(),name="login"),
    path('logout/',LogoutView.as_view(),name="logout"),

    path('password_change/', PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),

    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('password/',RedirectView.as_view(pattern_name='dj-auth:password_reset', permanent=False)),

    path('activate/<uidb64>/<token>/', ActivateAccount.as_view(), name='activate'),
    path('activate/resend/', ResendActivationEmail.as_view(), name='resend_activation'),
    path('activate/', RedirectView.as_view(pattern_name='dj-auth:resend_activation', permanent=False)),
    path('create/', CreateAccount.as_view(), name='create'),
    path('create/done/', TemplateView.as_view(template_name='users/user_create_done.html'), name='create_done'),
    path('disable/', DisableAccount.as_view(),name='disable'),

]

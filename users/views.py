from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.contrib.auth import get_user,get_user_model,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views import View
from django.urls import reverse_lazy
from .forms import UserCraeationForm, ResendActivationEmailForm
from .utils import  MailContextViewMixin
from django.views.decorators.debug import sensitive_post_parameters
from django.contrib.messages import error, success
from django.views.decorators.cache import never_cache
from django.utils.encoding import force_text
from django.utils.http import  urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator as token_generator
from resultMaker import settings

class LoginView(auth_views.LoginView):
    template_name = 'users/login.html'

class LogoutView(auth_views.LogoutView):

    template_name = 'users/logout.html'
    extra_context = {'form' : AuthenticationForm}


class PasswordChangeView(auth_views.PasswordChangeView):

    template_name = 'users/password_change_form.html'
    success_url = reverse_lazy('dj-auth:password_change_done')


class PasswordChangeDoneView(auth_views.PasswordChangeDoneView):
    template_name = 'users/password_change_done.html'


class PasswordResetView(auth_views.PasswordResetView):

    template_name = 'users/password_reset_form.html'
    email_template_name = 'users/password_reset_email.txt'
    subject_template_name = 'users/password_reset_subject.txt'
    success_url = reverse_lazy('dj-auth:password_reset_done')

class PasswordResetDoneView(auth_views.PasswordResetDoneView):

    template_name = 'users/password_reset_done.html'


class  PasswordResetConfirmView(auth_views.PasswordResetConfirmView):

    success_url = reverse_lazy('dj-auth:password_reset_complete')
    template_name = 'users/password_reset_confirm.html'


class PasswordResetCompleteView(auth_views.PasswordResetCompleteView):

    template_name = 'users/password_reset_complete.html'
    extra_context = {'form': AuthenticationForm }


class DisableAccount(View):

    success_url = settings.LOGIN_REDIRECT_URL
    template_name = 'users/user_confirm_delete.html'

    @method_decorator(csrf_protect)
    @method_decorator(login_required)
    def get(self, request):
        return TemplateResponse(request,self.template_name)

    def post(self,request):
        user = get_user(request)
        user.set_unusable_password()
        user.is_active = False
        user.save()
        logout(request)
        return redirect(self.success_url)


class CreateAccount(MailContextViewMixin, View):

    form_class = UserCraeationForm
    success_url =  reverse_lazy('dj-auth:create_done')
    template_name = 'users/user_create.html'


    @method_decorator(csrf_protect)
    def get(self, request):
        return TemplateResponse(request, self.template_name, context={'form' : self.form_class})


    @method_decorator(csrf_protect)
    @method_decorator(sensitive_post_parameters('password1', 'password2'))
    def post(self, request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            bound_form.save(**self.get_save_kwargs(request))
            if bound_form.mail_sent:
                return redirect(self.success_url)
            else:
                errs = (bound_form.non_field_errors())
                for err in errs:
                    error(request, err)
                return redirect('dj-auth:resend_activation')
        return TemplateResponse(request, self.template_name, context={'form' : bound_form})

class ActivateAccount(View):

    success_url = reverse_lazy('dj-auth:login')
    template_name = 'users/user_activate.html'

    @method_decorator(never_cache)
    def get(self, request, uidb64, token):
        
        User = get_user_model()
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk = uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist) :
            user = None
        if(user is not None and token_generator.check_token(user,token)):
            user.is_active = True
            user.save()
            success(request, 'User Activated! You may now login!')
            return redirect(self.success_url)
        else:
            return TemplateResponse(request, self.template_name)

class ResendActivationEmail(MailContextViewMixin, View):

    form_class = ResendActivationEmailForm
    success_url = reverse_lazy('dj-auth:login')
    template_name = 'users/resend_activation.html'

    @method_decorator(csrf_protect)
    def get(self, request):
        return TemplateResponse(request, self.template_name, {'form' : self.form_class})

    def post(self, request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            user = bound_form.save(**self.get_save_kwargs(request))
            if(user is not None and not bound_form.mail_sent):
                errs = (bound_form.non_field_errors())
                for err in errs:
                    error(request, err)
                if errs:
                    bound_form.errors.pop('__all__')
                return TemplateResponse(request, self.template_name, {'form':bound_form})
        success(request,'Activation Email Sent!')
        return redirect(self.success_url)
  

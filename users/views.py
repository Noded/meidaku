from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from . import forms


# Create your views here.


class LoginUser(LoginView):
    form_class = forms.LoginUserForm
    template_name = 'users/login.html'


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('main:index'))


class RegisterUser(CreateView):
    form_class = forms.RegisterUserForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

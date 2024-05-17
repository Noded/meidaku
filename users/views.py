from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from users.forms import LoginUserForm, RegisterUserForm


# Create your views here.


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'registration/login.html'
# def login_user(request):
#     if request.method == 'POST':
#         form = LoginUserForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request, username=cd['username'],
#                                 email=cd['email'],
#                                 password=cd['password'],
#                                 )
#             if user and user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect(reverse('main:index'))
#     else:
#         form = LoginUserForm()
#
#     return render(request, 'users/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('main:index'))


def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = RegisterUserForm()
    return render(request, 'users/register.html', {'form': form})

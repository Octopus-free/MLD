from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from .forms import RegistrationForm
from django.views.generic import CreateView
from .models import MLDUser
from django.urls import reverse_lazy


class UserLoginView(LoginView):
    template_name = 'ManagingUsers/login.html'


class UserCreateView(CreateView):
    model = MLDUser
    template_name = 'ManagingUsers/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('ManagingUsers:login')
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from .forms import RegistrationForm
from django.views.generic import CreateView, DetailView, ListView
from .models import MLDUser
from django.urls import reverse_lazy
from rest_framework.authtoken.models import Token


class UserLoginView(LoginView):
    template_name = 'ManagingUsers/login.html'


class UserCreateView(CreateView):
    model = MLDUser
    template_name = 'ManagingUsers/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('ManagingUsers:login')


class TokenListView(ListView):
    model = Token
    template_name = 'ManagingUsers/profile.html'
    fields = '__all__'




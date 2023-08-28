from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.models import User

from accounts.forms import RegistrationForm





class UserCreateView(CreateView):
    model = User
    template_name = "accounts/register.html"
    form_class = RegistrationForm
    success_url = reverse_lazy('home')

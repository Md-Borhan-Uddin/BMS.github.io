from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.models import User

from accounts.forms import RegistrationForm





class UserCreateView(CreateView):
    model = User
    template_name = "accounts/register.html"
    form_class = RegistrationForm

from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.models import User

from accounts.forms import RegistrationForm, TransactinForm
from accounts.models import Transaction





class UserCreateView(CreateView):
    model = User
    template_name = "accounts/register.html"
    form_class = RegistrationForm
    success_url = reverse_lazy('home')


class TransactionCreateView(CreateView):
    model = Transaction
    template_name = "accounts/transaction.html"
    form_class = TransactinForm

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        return super().form_valid(form)

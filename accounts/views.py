from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin



from accounts.constant import TransactionType
from accounts.forms import DepositForm, LoanForm, RegistrationForm, TransactinForm, WithdrawForm
from accounts.models import Transaction





class UserCreateView(CreateView):
    model = User
    template_name = "accounts/register.html"
    form_class = RegistrationForm
    success_url = reverse_lazy('home')


class TransactionMixin(LoginRequiredMixin,CreateView):
    model = Transaction
    title = None

    def get_form_kwargs(self) -> Dict[str, Any]:
        kwargs = super().get_form_kwargs()
        kwargs.update({'account':self.model.user})
        return kwargs



class LoanCreateView(TransactionMixin):
    model = Transaction
    template_name = "accounts/loan.html"
    form_class = LoanForm



    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form = form.save(commit=False)
        form.transaction_type = TransactionType.LOAN
        return super().form_valid(form)



class WithdrawCreateView(TransactionMixin):
    model = Transaction
    template_name = "accounts/withdraw.html"
    form_class = WithdrawForm



    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form = form.save(commit=False)
        form.transaction_type = TransactionType.LOAN
        return super().form_valid(form)


class DepositCreateView(TransactionMixin):
    model = Transaction
    template_name = "accounts/deposit.html"
    form_class = DepositForm



    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form = form.save(commit=False)
        form.transaction_type = TransactionType.LOAN
        return super().form_valid(form)



from typing import Any, Dict, Mapping, Optional, Type, Union
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList

from accounts.models import Transaction



class RegistrationForm(UserCreationForm):

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light"
    

class TransactinForm(forms.ModelForm):

    class Meta:
        model = Transaction
        fields = ('amount',)
    
    def __init__(self, *args, **kwargs):
        self.account = kwargs.pop('account')
        return super().__init__(*args, **kwargs)

class LoanForm(TransactinForm):

    def clean(self,*args, **kwargs):
        print(self.account)
        amount = self.cleaned_data.get('amount')
        if amount<300:
            raise forms.ValidationError('you do not get loan less then 300 ')
        return super().clean()
    


class WithdrawForm(TransactinForm):

    def clean(self,*args, **kwargs):
        print(kwargs)
        amount = self.cleaned_data.get('amount')
        if amount<300:
            raise forms.ValidationError('you do not get loan less then 300 ')
        return super().clean()
    

class DepositForm(TransactinForm):

    def clean(self,*args, **kwargs):
        print(kwargs)
        amount = self.cleaned_data.get('amount')
        if amount<300:
            raise forms.ValidationError('you do not get loan less then 300 ')
        return super().clean()
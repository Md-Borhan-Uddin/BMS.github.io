from typing import Any, Dict
from django.contrib.auth.forms import UserCreationForm
from django import forms

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



class LoanForm(TransactinForm):

    def clean(self):
        return super().clean()

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='accounts')
    account_id = models.IntegerField(_("AccountId"))
    balance = models.DecimalField(_('Balance'), default=0.0,max_digits=12,decimal_places=2)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

   
        

    def __str__(self) -> str:
        return self.user.username
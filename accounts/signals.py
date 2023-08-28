from django.db.models.signals import post_save
from django.contrib.auth.models import User

from datetime import datetime
from django.dispatch import receiver

from accounts.models import Account


@receiver(post_save,sender=User)
def create_account(sender, created, instance, **kwargs):
    if created:
        a_id = int(str(datetime.today().date()).replace('-','')+str(instance.pk))
        Account.objects.create(user=instance, account_id=a_id)
    
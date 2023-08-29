from django.db import models


class TransactionType(models.TextChoices):
    DEPOSIT = 'Deposit','Deposit'
    WITHDRAW = 'Withdraw','Withdraw'
    LOAN = 'Loan','Loan'
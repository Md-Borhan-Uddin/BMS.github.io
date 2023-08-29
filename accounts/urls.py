from django.urls import path
from accounts.views import TransactionCreateView, UserCreateView

app_name = 'accounts'

urlpatterns = [
    path("register/", UserCreateView.as_view(), name="register"),
    path("transaction/", TransactionCreateView.as_view(), name="transaction"),
]

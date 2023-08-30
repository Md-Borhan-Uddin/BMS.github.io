from django.urls import path
from accounts.views import UserCreateView,LoanCreateView,WithdrawCreateView,DepositCreateView

app_name = 'accounts'

urlpatterns = [
    path("register/", UserCreateView.as_view(), name="register"),
    path("loan/", LoanCreateView.as_view(), name="loan"),
    path("withdraw/", WithdrawCreateView.as_view(), name="withdraw"),
    path("deposit/", DepositCreateView.as_view(), name="deposit"),
]

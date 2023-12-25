from django.urls import path

from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('registration', RegistrationPageView.as_view(), name='registration'),
    path("login", LoginPageView.as_view(), name='login'),
    path("login/secure-code", send_secure_code, name='send_secure_code'),
    path("logout", auth_logout, name='logout'),
    path("accounts", AccountsPageView.as_view(), name='accounts'),
    path("creating-bank-account", creating_bank_account, name='create_account'),
    path("create-card", create_card, name='create_card'),
    path("credit", CreditPageView.as_view(), name='credit'),
    path("credit/<int:active_card>", CreditPageView.as_view(), name='credit'),
    path("credit-dates", calculate_credit_dates, name='calculate_credit_dates'),
    path("transactions", TransactionsPageView.as_view(), name='transactions'),
    path("transactions/<int:active_card>", TransactionsPageView.as_view(), name='transactions'),
    path("make_transaction", make_transaction, name='make_transaction'),
]
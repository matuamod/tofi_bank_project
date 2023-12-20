from django.db import models
from django.contrib.auth.models import AbstractUser


class Role(models.Model):
    name = models.CharField(max_length=32)


class User(AbstractUser):
    REQUIRED_FIELDS = ('given_name', 'surname', 'father_name', 'phone_number')
    USERNAME_FIELD = 'username'

    given_name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    father_name = models.CharField(max_length=32)
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=16, unique=True)
    is_blocked = models.BooleanField(default=False)
    passport_number = models.CharField(max_length=10, unique=True)
    identification_number = models.CharField(max_length=14, unique=True)
    secure_code = models.CharField(max_length=256, null=True)
    role = models.ForeignKey("Role", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.first_name
    
    
class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    account_number = models.CharField(max_length=16, unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.account_number


class Card(models.Model):
    user = models.ForeignKey("User", on_delete=models.SET_NULL, null=True)
    given_name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    number = models.CharField(max_length=16)
    expire_date = models.DateField()
    cvv_code = models.CharField(max_length=256)
    account = models.ForeignKey("Account", on_delete=models.CASCADE, related_name='cards')


class Credit(models.Model):
    user = models.ForeignKey("User", on_delete=models.PROTECT)
    credit_sum = models.DecimalField(max_digits=10, decimal_places=2)
    start_payment_date = models.DateField(auto_now=True)
    credit_term = models.IntegerField()
    percent = models.DecimalField(max_digits=5, decimal_places=2)
    is_approved = models.BooleanField(default=False)


class Logs(models.Model):
    action_date = models.DateTimeField()
    action = models.CharField(max_length=256)


class Transactions(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    card_from = models.ForeignKey("Card", on_delete=models.CASCADE, related_name='card_from')
    card_to = models.ForeignKey("Card", on_delete=models.CASCADE, related_name='card_to')


class UserHistory(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    action_date = models.DateTimeField()
    action = models.CharField(max_length=256)

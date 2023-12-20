from django.test import TestCase, Client
from django.urls import reverse
from decimal import *
from .models import *
from datetime import date, datetime, timedelta
import random
import hashlib

class BankTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('test_user', given_name="Ihar", surname="Iharov", father_name="Iharovich", password='testpass')
        self.client.login(username='test_user', password='testpass')

        self.client.post(reverse('create_account'))
        self.user_account = Account.objects.get(user=self.user)
        response = self.client.post(reverse('create_card'), {'account_id': self.user_account.id})
        self.user_card = Card.objects.get(account=self.user_account)
        self.user_card.balance = Decimal(10000)

        self.receiver_user = User.objects.create_user(passport_number='MC3044487',
                                                      identification_number='5171202PB113B3', 
                                                      username='second_user', 
                                                      given_name="Oleg", 
                                                      surname="Olegov", 
                                                      father_name="Olegovich", 
                                                      password='testpass',
                                                      email="matua.models2003@gmail.com",
                                                      phone_number="+375253353333")
        self.receiver_account = Account.objects.create(user=self.receiver_user, account_number="333", balance=Decimal(1000))

        cvv_code_source = random.randint(0, 999)
        cvv_code = str(cvv_code_source).zfill(3)
        cvv_code = hashlib.sha256(cvv_code.encode('utf-8')).hexdigest()

        self.receiver_card = Card.objects.create(user=self.receiver_user, 
                                                 given_name="Oleg", 
                                                 surname="Olegov",
                                                 number="1234432112344321",
                                                 expire_date=date(datetime.now().year + 3, datetime.now().month, 31),
                                                 cvv_code=cvv_code,
                                                 account=self.receiver_account)

    def tearDown(self):
        self.client.logout()

    def test_user_password(self):
        user = User.objects.get(username='test_user')
        self.assertTrue(user.check_password('testpass'))

    def test_main_view(self):
        response = self.client.get(f'')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
        
    def test_register_view(self):
        response = self.client.get(f'/registration')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/index.html')

    def test_login_view(self):
        response = self.client.get(f'/login')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login/index.html')

    def test_bank_account(self):
        response = self.client.post(reverse('create_account'))
        self.assertEqual(response.status_code, 302)

    def test_create_card(self):
        self.client.post(reverse('create_account'))
        self.account = Account.objects.latest('pk')
        response = self.client.post(reverse('create_card'), {'account_id': self.account.id})

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'card/index.html')

        self.assertTrue(Card.objects.filter(account=self.account, user=self.user).exists())

    def test_auth_logout(self):
        response = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code, 302)

    def test_make_transaction(self):
        response = self.client.post(reverse('make_transaction'), {'sender_card': self.user_card.number, 'card_number': self.receiver_card.number, 'sum': '1000000'})
        self.assertEqual(Transactions.objects.all().count(), 0)

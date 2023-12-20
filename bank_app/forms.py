from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import *

form_attr = {'class': 'form-control'}

class RegistrationForm(UserCreationForm):

    given_name = forms.CharField(label='Given name', widget=forms.TextInput(attrs=form_attr))
    surname = forms.CharField(label='Surname', widget=forms.TextInput(attrs=form_attr))
    father_name = forms.CharField(label='Father name', widget=forms.TextInput(attrs=form_attr))
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs=form_attr))
    email = forms.CharField(label='Email', widget=forms.EmailInput(attrs=form_attr))
    phone_number = forms.CharField(label='Telephone number', widget=forms.TextInput(attrs=form_attr))
    passport_number = forms.CharField(label='Passport number', widget=forms.TextInput(attrs=form_attr))
    identification_number = forms.CharField(label='Identification number', widget=forms.TextInput(attrs=form_attr))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs=form_attr))
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs=form_attr))

    class Meta:
        model = User
        fields = ('given_name', 'surname', 'father_name', 'username', 'email', 'phone_number', 'passport_number', 'identification_number', 'password1', 'password2')


class LoginForm(AuthenticationForm):

    username = forms.CharField(label='Username', widget=forms.TextInput(attrs=form_attr))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs=form_attr))
    secure_code = forms.CharField(label='Security code', max_length=10, required=True, widget=forms.TextInput(attrs=form_attr))
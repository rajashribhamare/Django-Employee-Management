from django import forms
from .models import Customer, Account, Transaction

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = '__all__'

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'



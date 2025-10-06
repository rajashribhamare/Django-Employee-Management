from django import forms

class DepositForm(forms.Form):
    amount = forms.DecimalField(max_digits=10, decimal_places=2, min_value=0.01)

class WithdrawForm(forms.Form):
    amount = forms.DecimalField(max_digits=10, decimal_places=2, min_value=0.01)

class TransferForm(forms.Form):
    to_account = forms.CharField(max_length=12) 
    amount = forms.DecimalField(max_digits=10, decimal_places=2, min_value=0.01)

from django.shortcuts import render,redirect
from .models import Customer, Account, Transaction
from .forms import CustomerForm, AccountForm, TransactionForm

# View to List Customers
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer_list.html', {'customers': customers})

# View to Add a New Customer
def add_customer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'add_customer.html', {'form': form})

# View to List Accounts
def account_list(request):
    accounts = Account.objects.all()
    return render(request, 'account_list.html', {'accounts': accounts})

# View to Add an Account
def add_account(request):
    if request.method == "POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account_list')
    else:
        form = AccountForm()
    return render(request, 'add_account.html', {'form': form})

# View to Handle Transactions
def add_transaction(request):
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save()
            # Update account balance
            if transaction.transaction_type == 'deposit':
                transaction.account.balance += transaction.amount
            elif transaction.transaction_type == 'withdrawal':
                if transaction.account.balance >= transaction.amount:
                    transaction.account.balance -= transaction.amount
                else:
                    return render(request, 'transaction_error.html', {'error': 'Insufficient balance'})
            transaction.account.save()
            return redirect('account_list')
    else:
        form = TransactionForm()
    return render(request, 'add_transaction.html', {'form': form})

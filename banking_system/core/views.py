from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Customer, Transaction
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import TransferForm , WithdrawForm , DepositForm


@login_required
def dashboard(request):
    customer = Customer.objects.get(user=request.user)
    transactions = Transaction.objects.filter(customer=customer).order_by('-timestamp')[:10]
    return render(request, 'dashboard.html', {
        'customer': customer,
        'transactions': transactions
    })
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            account_number = str(user.id).zfill(10)
            from .models import Customer  # Local import to avoid circular issues
            Customer.objects.create(user=user, account_number=account_number)
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def deposit_view(request):
    if request.method == 'POST':
        form = DepositForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            customer = Customer.objects.get(user=request.user)
            customer.balance += amount
            customer.save()
            Transaction.objects.create(
                customer=customer,
                transaction_type='DEPOSIT',
                amount=amount
            )
            messages.success(request, f'Deposit of ₹{amount} successful.')
            return redirect('dashboard')
    else:
        form = DepositForm()
    return render(request, 'deposit.html', {'form': form})



@login_required
def withdraw_view(request):
    if request.method == 'POST':
        form = WithdrawForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            customer = Customer.objects.get(user=request.user)
            if customer.balance >= amount:
                customer.balance -= amount
                customer.save()
                Transaction.objects.create(
                    customer=customer,
                    transaction_type='WITHDRAW',
                    amount=amount
                )
                messages.success(request, f'Withdrawal of ₹{amount} successful.')
                return redirect('dashboard')
            else:
                messages.error(request, 'Insufficient balance.')
    else:
        form = WithdrawForm()
    return render(request, 'withdraw.html', {'form': form})



@login_required
def transfer_view(request):
    if request.method == 'POST':
        form = TransferForm(request.POST)
        if form.is_valid():
            to_account = form.cleaned_data['to_account']
            amount = form.cleaned_data['amount']

            sender = Customer.objects.get(user=request.user)
            try:
                receiver = Customer.objects.get(account_number=to_account)
            except Customer.DoesNotExist:
                messages.error(request, 'Receiver account not found.')
                return redirect('transfer')

            if sender.balance >= amount:
                sender.balance -= amount
                receiver.balance += amount
                sender.save()
                receiver.save()

                # Log both transactions
                Transaction.objects.create(customer=sender, transaction_type='TRANSFER_OUT', amount=amount)
                Transaction.objects.create(customer=receiver, transaction_type='TRANSFER_IN', amount=amount)

                messages.success(request, f'Successfully transferred ₹{amount} to {receiver.user.username}.')
                return redirect('dashboard')
            else:
                messages.error(request, 'Insufficient balance.')
    else:
        form = TransferForm()
    
    return render(request, 'transfer.html', {'form': form})
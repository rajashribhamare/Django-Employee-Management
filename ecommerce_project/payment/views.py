import razorpay
from django.conf import settings
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

def start_payment(request):
    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
    order_amount = 50000  # 500 INR in paise
    order_currency = 'INR'
    order = client.order.create(dict(amount=order_amount, currency=order_currency, payment_capture='1'))

    return render(request, "payment/payment.html", {
        "order_id": order["id"],
        "amount": order_amount,
        "key_id": settings.RAZORPAY_KEY_ID,
        "currency": order_currency
    })

@csrf_exempt
def payment_success(request):
    return render(request, "payment/success.html")

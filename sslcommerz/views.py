from django.shortcuts import render
from django.urls import reverse

from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import random
import string
from .models import Payment

# from .models import Patient, User
from sslcommerz_lib import SSLCOMMERZ
settings = {'store_id': 'fidal5ed892039802d',
            'store_pass': 'fidal5ed892039802d@ssl', 'issandbox': True}
sslcz = SSLCOMMERZ(settings)

# Store_Name = 'testfidalyk5v'

# Create your views here.
"""
Also learn how to bring store data using environment variables.

Learn how to apply two decorators to a single view function.
in this case --> @login_required and @csrf_exempt    
"""
payment = Payment()


def generate_random_string():
    N = 8
    string_var = ""
    string_var = ''.join(random.choices(
        string.ascii_uppercase + string.digits, k=N))
    string_var = "SSLCZ_TEST_" + string_var
    return string_var


def generate_random_val_id():
    N = 12
    string_var = ""
    string_var = ''.join(random.choices(
        string.ascii_uppercase + string.digits, k=N))
    return string_var


# def payment_home(request):
#     return render(request, 'payment_index.html')

# @login_required


@csrf_exempt
def ssl_payment_request(request):
    """
    1) Create a Initial Payment Request Session

    This view function is used to create a payment request. (Checkout or Pay now will be redirect to this url and view function)

    post_body is all the information of the payment request, including amount and customer details
    """

    """
    Additional code to be added later (examples):
    1) saved_address = BillingAddress.objects.get_or_create(user=request.user)
    2) profile = request.user.profile ---> get the user profile of logged in user
    """

    post_body = {}
    post_body['total_amount'] = 200
    post_body['currency'] = "BDT"
    post_body['tran_id'] = generate_random_string()

    post_body['success_url'] = request.build_absolute_uri(
        reverse('ssl-payment-success'))
    post_body['fail_url'] = request.build_absolute_uri(
        reverse('ssl-payment-fail'))
    post_body['cancel_url'] = request.build_absolute_uri(
        reverse('ssl-payment-cancel'))

    post_body['emi_option'] = 0
    """
    Customer Information Must be saved to the database first as these are not recovered during ipn
    """
    post_body['cus_name'] = "Mohammed Jawwadul Islam"
    post_body['cus_email'] = "jawwad@gmail.com"
    post_body['cus_phone'] = "0175462156"
    post_body['cus_add1'] = "Shankor, Dhanmondi"
    post_body['cus_city'] = "Dhaka"
    post_body['cus_country'] = "Bangladesh"
    post_body['shipping_method'] = "NO"
    # post_body['multi_card_name'] = ""
    post_body['num_of_item'] = 1
    post_body['product_name'] = "Test"
    post_body['product_category'] = "Test Category"
    post_body['product_profile'] = "general"

    # Save in database

    payment.name = post_body['cus_name']
    payment.email = post_body['cus_email']
    payment.phone = post_body['cus_phone']
    payment.address = post_body['cus_add1']
    payment.city = post_body['cus_city']
    payment.country = post_body['cus_country']
    payment.save()

    response = sslcz.createSession(post_body)  # API response
    print(response)

    return redirect(response['GatewayPageURL'])

    # return render(request, 'checkout.html')

# @login_required


@csrf_exempt
def ssl_payment_success(request):
    """
    2) Validate payment with IPN

    Sucess page for payment request
    getting the payment data from the request (previous post_body information)
    """

    # http://127.0.0.1:8000/ssl-payment-success/
    # link = request.build_absolute_uri(reverse('ssl-payment-success'))

    payment_data = request.POST
    status = payment_data['status']

    if status == 'VALID':
        tran_id = payment_data['tran_id']
        """
        Fields we need from payment_data
        
        payment_data['tran_id']
        payment_data['val_id']
        payment_data['amount']
        payment_data['card_type']
        payment_data['card_no']
        payment_data['bank_tran_id']
        payment_data['status']
        payment_data['tran_date']
        payment_data['currency']
        payment_data['card_issuer']
        payment_data['card_brand']
        payment_data['card_issuer_country']
        payment_data['currency_type']
        payment_data['currency_amount']
        """

        # Save in Database
        # payment = Payment()

        payment.transaction_id = payment_data['tran_id']
        payment.val_transaction_id = payment_data['val_id']
        payment.currency_amount = payment_data['currency_amount']
        payment.card_type = payment_data['card_type']
        payment.card_no = payment_data['card_no']
        payment.bank_transaction_id = payment_data['bank_tran_id']
        payment.status = payment_data['status']
        payment.transaction_date = payment_data['tran_date']
        payment.currency = payment_data['currency']
        payment.card_issuer = payment_data['card_issuer']
        payment.card_brand = payment_data['card_brand']
        payment.save()

        dic = {'payment_data': payment_data}
        return render(request, 'success.html', dic)

    elif status == 'FAILED':
        redirect('ssl-payment-fail')


# @login_required


@csrf_exempt
def ssl_payment_fail(request):
    return render(request, 'fail.html')

# @login_required


@csrf_exempt
def ssl_payment_cancel(request):
    return render(request, 'cancel.html')

from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import random
import string
from .models import Payment
from hospital.models import Patient
from pharmacy.models import Order, Cart
from doctor.models import Appointment, Prescription, Prescription_test, testCart, testOrder 
from django.contrib.auth.decorators import login_required


from django.core.mail import BadHeaderError, send_mail
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.utils.html import strip_tags


# from .models import Patient, User
from sslcommerz_lib import SSLCOMMERZ
from django.conf import settings


STORE_ID = settings.STORE_ID
STORE_PASSWORD = settings.STORE_PASSWORD
STORE_NAME = settings.STORE_NAME

payment_settings = {'store_id': STORE_ID,
            'store_pass': STORE_PASSWORD, 'issandbox': True}

sslcz = SSLCOMMERZ(payment_settings)


# Create your views here.



def generate_random_string():
    N = 8
    string_var = ""
    string_var = ''.join(random.choices(
        string.ascii_uppercase + string.digits, k=N))
    string_var = "SSLCZ_TEST_" + string_var
    return string_var

def generate_random_invoice():
    N = 4
    string_var = ""
    string_var = ''.join(random.choices(string.digits, k=N))
    string_var = "#INV-" + string_var
    return string_var


def generate_random_val_id():
    N = 12
    string_var = ""
    string_var = ''.join(random.choices(
        string.ascii_uppercase + string.digits, k=N))
    return string_var


def payment_home(request):
    return render(request, 'index.html')

# @login_required


@csrf_exempt
def ssl_payment_request(request, pk, id):
    # Payment Request for appointment payment
    """
    1) Create a Initial Payment Request Session

    This view function is used to create a payment request. (Checkout or Pay now will be redirect to this url and view function)
    """

    """
    Additional code to be added later (examples):
    1) saved_address = BillingAddress.objects.get_or_create(user=request.user)
    """
    
    
    patient = Patient.objects.get(patient_id=pk)
    appointment = Appointment.objects.get(id=id)
    
    invoice_number = generate_random_invoice()
    
    post_body = {}
    post_body['total_amount'] = appointment.doctor.consultation_fee + appointment.doctor.report_fee
    post_body['currency'] = "BDT"
    post_body['tran_id'] = generate_random_string()

    post_body['success_url'] = request.build_absolute_uri(
        reverse('ssl-payment-success'))
    post_body['fail_url'] = request.build_absolute_uri(
        reverse('ssl-payment-fail'))
    post_body['cancel_url'] = request.build_absolute_uri(
        reverse('ssl-payment-cancel'))

    post_body['emi_option'] = 0
  
    post_body['cus_name'] = patient.username
    post_body['cus_email'] = patient.email
    post_body['cus_phone'] = patient.phone_number
    post_body['cus_add1'] = patient.address
    post_body['cus_city'] = "Dhaka"
    post_body['cus_country'] = "Bangladesh"
    post_body['shipping_method'] = "NO"
    # post_body['multi_card_name'] = ""
    post_body['num_of_item'] = 1
    post_body['product_name'] = "Test"
    post_body['product_category'] = "Test Category"
    post_body['product_profile'] = "general"

    # Save in database
    appointment.transaction_id = post_body['tran_id']
    appointment.save()
    
    payment = Payment()
    # payment.patient_id = patient.patient_id
    # payment.appointment_id = appointment.id
    payment.patient = patient
    payment.appointment = appointment
    payment.name = post_body['cus_name']
    payment.email = post_body['cus_email']
    payment.phone = post_body['cus_phone']
    payment.address = post_body['cus_add1']
    payment.city = post_body['cus_city']
    payment.country = post_body['cus_country']
    payment.transaction_id = post_body['tran_id']
    
    payment.consulation_fee = appointment.doctor.consultation_fee
    payment.report_fee = appointment.doctor.report_fee
    payment.invoice_number = invoice_number
    
    payment_type = "appointment"
    payment.payment_type = payment_type
    payment.save()
    
    
    response = sslcz.createSession(post_body)  # API response
    print(response)

    return redirect(response['GatewayPageURL'])

    # return render(request, 'checkout.html')


@csrf_exempt
def ssl_payment_request_medicine(request, pk, id):
    # Payment Request for appointment payment
    
    patient = Patient.objects.get(patient_id=pk)
    order = Order.objects.get(id=id)
    
    invoice_number = generate_random_invoice()
    
    post_body = {}
    post_body['total_amount'] = order.final_bill()
    post_body['currency'] = "BDT"
    post_body['tran_id'] = generate_random_string()

    post_body['success_url'] = request.build_absolute_uri(
        reverse('ssl-payment-success'))
    post_body['fail_url'] = request.build_absolute_uri(
        reverse('ssl-payment-fail'))
    post_body['cancel_url'] = request.build_absolute_uri(
        reverse('ssl-payment-cancel'))

    post_body['emi_option'] = 0
  
    post_body['cus_name'] = patient.username
    post_body['cus_email'] = patient.email
    post_body['cus_phone'] = patient.phone_number
    post_body['cus_add1'] = patient.address
    post_body['cus_city'] = "Dhaka"
    post_body['cus_country'] = "Bangladesh"
    post_body['shipping_method'] = "NO"
    # post_body['multi_card_name'] = ""
    post_body['num_of_item'] = 1
    post_body['product_name'] = "Test"
    post_body['product_category'] = "Test Category"
    post_body['product_profile'] = "general"

    # Save in database
    order.trans_ID = post_body['tran_id']
    order.save()
    
    payment = Payment()
    # payment.patient_id = patient.patient_id
    # payment.appointment_id = appointment.id
    payment.patient = patient
    # payment.appointment = appointment
    payment.name = post_body['cus_name']
    payment.email = post_body['cus_email']
    payment.phone = post_body['cus_phone']
    payment.address = post_body['cus_add1']
    payment.city = post_body['cus_city']
    payment.country = post_body['cus_country']
    payment.transaction_id = post_body['tran_id']
    
    # payment.consulation_fee = appointment.doctor.consultation_fee
    # payment.report_fee = appointment.doctor.report_fee
    payment.invoice_number = invoice_number
    
    payment_type = "pharmacy"
    payment.payment_type = payment_type
    payment.save()
    
    
    response = sslcz.createSession(post_body)  # API response
    print(response)

    return redirect(response['GatewayPageURL'])


@csrf_exempt
def ssl_payment_request_test(request, pk, id, pk2):
    # Payment Request for test payment
    
    patient = Patient.objects.get(patient_id=pk)
    test_order = testOrder.objects.get(id=id)
    prescription = Prescription.objects.get(prescription_id=pk2)
    
    invoice_number = generate_random_invoice()
    
    post_body = {}
    post_body['total_amount'] = test_order.final_bill()
    post_body['currency'] = "BDT"
    post_body['tran_id'] = generate_random_string()

    post_body['success_url'] = request.build_absolute_uri(
        reverse('ssl-payment-success'))
    post_body['fail_url'] = request.build_absolute_uri(
        reverse('ssl-payment-fail'))
    post_body['cancel_url'] = request.build_absolute_uri(
        reverse('ssl-payment-cancel'))

    post_body['emi_option'] = 0
  
    post_body['cus_name'] = patient.username
    post_body['cus_email'] = patient.email
    post_body['cus_phone'] = patient.phone_number
    post_body['cus_add1'] = patient.address
    post_body['cus_city'] = "Dhaka"
    post_body['cus_country'] = "Bangladesh"
    post_body['shipping_method'] = "NO"
    # post_body['multi_card_name'] = ""
    post_body['num_of_item'] = 1
    post_body['product_name'] = "Test"
    post_body['product_category'] = "Test Category"
    post_body['product_profile'] = "general"

    # Save in database
    test_order.trans_ID = post_body['tran_id']
    test_order.save()
    
    payment = Payment()
    # payment.patient_id = patient.patient_id
    # payment.appointment_id = appointment.id
    payment.patient = patient
    # payment.appointment = appointment
    payment.name = post_body['cus_name']
    payment.email = post_body['cus_email']
    payment.phone = post_body['cus_phone']
    payment.address = post_body['cus_add1']
    payment.city = post_body['cus_city']
    payment.country = post_body['cus_country']
    payment.transaction_id = post_body['tran_id']
    payment.prescription = prescription
    
    # payment.consulation_fee = appointment.doctor.consultation_fee
    # payment.report_fee = appointment.doctor.report_fee
    payment.invoice_number = invoice_number
    
    payment_type = "test"
    payment.payment_type = payment_type
    payment.save()
    
    
    response = sslcz.createSession(post_body)  # API response
    print(response)

    return redirect(response['GatewayPageURL'])    

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

        # Update Database
        payment = Payment.objects.get(transaction_id=tran_id)
        
        payment_type = payment.payment_type
        
        if payment_type == "appointment":
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
            
            appointment = Appointment.objects.get(transaction_id=tran_id)
            appointment.transaction_id = tran_id
            appointment.payment_status = "VALID"
            appointment.save()
            
    
            if sslcz.hash_validate_ipn(payment_data):
                response = sslcz.validationTransactionOrder(payment_data['val_id'])
                print(response)
            else:
                print("Hash validation failed")

            #dic = {'payment_data': payment_data, 'response': response}
            #return render(request, 'success.html', dic)
            
            # Mailtrap
            patient_email = payment.patient.email
            patient_name = payment.patient.name
            patient_username = payment.patient.username
            patient_phone_number = payment.patient.phone_number
            doctor_name = appointment.doctor.name
        
            subject = "Payment Receipt for appointment"
            
            values = {
                    "email":patient_email,
                    "name":patient_name,
                    "username":patient_username,
                    "phone_number":patient_phone_number,
                    "doctor_name":doctor_name,
                    "tran_id":payment_data['tran_id'],
                    "currency_amount":payment_data['currency_amount'],
                    "card_type":payment_data['card_type'],
                    "bank_transaction_id":payment_data['bank_tran_id'],
                    "transaction_date":payment_data['tran_date'],
                    "card_issuer":payment_data['card_issuer'],
                }
            
            html_message = render_to_string('appointment_mail_payment_template.html', {'values': values})
            plain_message = strip_tags(html_message)
            
            try:
                send_mail(subject, plain_message, 'hospital_admin@gmail.com',  [patient_email], html_message=html_message, fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found')
    
            return redirect('patient-dashboard')
        
        elif payment_type == "test":
            prescription = payment.prescription
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
            
            test_order = testOrder.objects.get(trans_ID=tran_id)
            test_order.payment_status = "VALID"
            test_order.save()
    
            if sslcz.hash_validate_ipn(payment_data):
                response = sslcz.validationTransactionOrder(payment_data['val_id'])
                print(response)
            else:
                print("Hash validation failed")
                
            # # Mailtrap
            patient_email = payment.patient.email
            patient_name = payment.patient.name
            patient_username = payment.patient.username
            patient_phone_number = payment.patient.phone_number
            
            ob = testCart.objects.filter(testorder__trans_ID=tran_id)
            len_ob = len(ob)
            
            # list_id = []
            # list_name = []
            # for i in range(len_ob):
            #     list_id.append(ob[i].item.test_info_id)
            #     list_name.append(ob[i].item.test_name)
                
            order_cart = []   
            for i in range(len_ob):
                order_cart.append(ob[i])
                
            for i in order_cart:
                test_id = i.item.test_info_id
                pres_test = Prescription_test.objects.filter(prescription=prescription).filter(test_info_id=test_id)
                #pres_test.test_info_pay_status = "Paid"
                pres_test.update(test_info_id=test_id,test_info_pay_status = "Paid")
            
        
            subject = "Payment Receipt for test"
            
            values = {
                    "email":patient_email,
                    "name":patient_name,
                    "username":patient_username,
                    "phone_number":patient_phone_number,
                    "tran_id":payment_data['tran_id'],
                    "currency_amount":payment_data['currency_amount'],
                    "card_type":payment_data['card_type'],
                    "bank_transaction_id":payment_data['bank_tran_id'],
                    "transaction_date":payment_data['tran_date'],
                    "card_issuer":payment_data['card_issuer'],
                    "order_cart":order_cart,
                }
            
            html_message = render_to_string('test_mail_payment_template.html', {'values': values})
            plain_message = strip_tags(html_message)
            
            try:
                send_mail(subject, plain_message, 'hospital_admin@gmail.com',  [patient_email], html_message=html_message, fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            
            # Reset cart
            testCart.objects.all().delete()
                
            return redirect('patient-dashboard')
            
            
        elif payment_type == "pharmacy":
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
            
            order = Order.objects.get(trans_ID=tran_id)
            order.payment_status = "VALID"
            order.save()
    
            if sslcz.hash_validate_ipn(payment_data):
                response = sslcz.validationTransactionOrder(payment_data['val_id'])
                print(response)
            else:
                print("Hash validation failed")
                
            # Mailtrap
            patient_email = payment.patient.email
            patient_name = payment.patient.name
            patient_username = payment.patient.username
            patient_phone_number = payment.patient.phone_number
            
            ob = Cart.objects.filter(order__trans_ID=tran_id)
            len_ob = len(ob)
            
            # list_id = []
            # list_name = []
            # for i in range(len_ob):
            #     list_id.append(ob[i].item.serial_number)
            #     list_name.append(ob[i].item.name)
                
            order_cart = []   
            for i in range(len_ob):
                order_cart.append(ob[i])
            
        
            subject = "Payment Receipt for pharmacy"
            
            values = {
                    "email":patient_email,
                    "name":patient_name,
                    "username":patient_username,
                    "phone_number":patient_phone_number,
                    "tran_id":payment_data['tran_id'],
                    "currency_amount":payment_data['currency_amount'],
                    "card_type":payment_data['card_type'],
                    "bank_transaction_id":payment_data['bank_tran_id'],
                    "transaction_date":payment_data['tran_date'],
                    "card_issuer":payment_data['card_issuer'],
                    "order_cart":order_cart,
                }
            
            html_message = render_to_string('pharmacy_mail_payment_template.html', {'values': values})
            plain_message = strip_tags(html_message)
            
            try:
                send_mail(subject, plain_message, 'hospital_admin@gmail.com',  [patient_email], html_message=html_message, fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            
            # Reset cart
            Cart.objects.all().delete()
                
            return redirect('patient-dashboard')

    elif status == 'FAILED':
        redirect('ssl-payment-fail')





@csrf_exempt
def ssl_payment_fail(request):
    return render(request, 'fail.html')

# @login_required


@csrf_exempt
def ssl_payment_cancel(request):
    return render(request, 'cancel.html')

@csrf_exempt
def payment_testing(request, pk):
    # order = Order.objects.get(id=pk)
    # ob = Cart.objects.filter(order__id=pk)
    
    tran_id = "SSLCZ_TEST_TGJOWR8G"
    # tran_id = "SSLCZ_TEST_74D530YZ"
    #ob = Cart.objects.filter(order__trans_ID=tran_id)
    ob = testCart.objects.filter(testorder__trans_ID=tran_id)
    

    len_ob = len(ob)
    
    list_id = []
    list_name = []
    for i in range(len_ob):
        list_id.append(ob[i].item.test_info_id)
        list_name.append(ob[i].item.test_name)
    
    order_cart = []   
    for i in range(len_ob):
        order_cart.append(ob[i])
    
    context = {'order': ob, 'len_ob': len_ob, 'list_id': list_id, 'list_name': list_name, 'order_cart': order_cart}

    return render(request, 'testing.html', context)

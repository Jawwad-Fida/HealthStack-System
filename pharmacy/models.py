from django.db import models
from django.conf import settings
import uuid
from doctor.models import Prescription

from hospital.models import User, Patient


# Create your models here.

class Pharmacist(models.Model):
    pharmacist_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name='pharmacist')
    name = models.CharField(max_length=200, null=True, blank=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    degree = models.CharField(max_length=200, null=True, blank=True)
    featured_image = models.ImageField(upload_to='doctors/', default='pharmacist/user-default.png', null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.user.username)


class Medicine(models.Model):
    MEDICINE_TYPE = (
        ('tablets', 'tablets'),
        ('syrup', 'syrup'),
        ('capsule', 'capsule'),
        ('general', 'general'),
    )
    REQUIREMENT_TYPE = (
        ('yes', 'yes'),
        ('no', 'no'),
    )
    
    MEDICINE_CATEGORY = (
        ('fever', 'fever'),
        ('pain', 'pain'),
        ('cough', 'cough'),
        ('cold', 'cold'),
        ('flu', 'flu'),
        ('diabetes', 'diabetes'),
        ('eye', 'eye'),
        ('ear', 'ear'),
        ('allergy', 'allergy'),
        ('asthma', 'asthma'),
        ('bloodpressure', 'bloodpressure'),
        ('heartdisease', 'heartdisease'),
        ('vitamins', 'vitamins'),
        ('digestivehealth', 'digestivehealth'),
        ('skin', 'skin'),
        ('infection', 'infection'),
        ('nurological', 'nurological'),
    )
    
    serial_number = models.AutoField(primary_key=True)
    medicine_id = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    weight = models.CharField(max_length=200, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True, default=0)
    featured_image = models.ImageField(upload_to='medicines/', default='medicines/default.png', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    medicine_type = models.CharField(max_length=200, choices=MEDICINE_TYPE, null=True, blank=True)
    medicine_category = models.CharField(max_length=200, choices=MEDICINE_CATEGORY, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True, default=0)
    stock_quantity = models.IntegerField(null=True, blank=True, default=0)
    Prescription_reqiuired = models.CharField(max_length=200, choices=REQUIREMENT_TYPE, null=True, blank=True)
    def __str__(self):
        return str(self.name)
    

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cart')
    item = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    purchased = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.quantity} X {self.item}'
    
    # Each product total
    def get_total(self):
        total = self.item.price * self.quantity
        float_total = format(total, '0.2f')
        return float_total
    

class Order(models.Model):
    # id
    orderitems = models.ManyToManyField(Cart)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=200, blank=True, null=True)
    trans_ID = models.CharField(max_length=200, blank=True, null=True)

    # Subtotal
    def get_totals(self):
        total = 0 
        for order_item in self.orderitems.all():
            total += float(order_item.get_total())
        return total
    
    # Count Cart Items
    def count_cart_items(self):
        return self.orderitems.count()
    
    # Stock Calculation
    def stock_quantity_decrease(self):
        for order_item in self.orderitems.all():
            decrease_stock= order_item.item.stock_quantity - order_item.quantity
            order_item.item.stock_quantity = decrease_stock 
            order_item.item.stock_quantity.save()
            return decrease_stock
    
    # TOTAL
    def final_bill(self):
        delivery_price= 40.00
        Bill = self.get_totals()+ delivery_price
        float_Bill = format(Bill, '0.2f')
        return float_Bill
    

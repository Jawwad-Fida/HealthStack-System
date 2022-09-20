# Welcome to Pharmacist


##  The main duties of a pharmacist includes:

* `Administrative tasks such as add medicines information.`
* `Edit medicine information.`
* `Delete medicine information.`
* `Search medicine.`
* `View Medicine information.`


## Add medicines into database
```python
def add_medicine(request):
    if request.user.is_pharmacist:
     user = Pharmacist.objects.get(user=request.user)
     
    if request.method == 'POST':
       medicine = Medicine()
       
       if 'featured_image' in request.FILES:
           featured_image = request.FILES['featured_image']
       else:
           featured_image = "medicines/default.png"
       
       name = request.POST.get('name')
       Prescription_reqiuired = request.POST.get('requirement_type')     
       weight = request.POST.get('weight') 
       quantity = request.POST.get('quantity')
       medicine_category = request.POST.get('category_type')
       medicine_type = request.POST.get('medicine_type')
       description = request.POST.get('description')
       price = request.POST.get('price')
       
       medicine.name = name
       medicine.Prescription_reqiuired = Prescription_reqiuired
       medicine.weight = weight
       medicine.quantity = quantity
       medicine.medicine_category = medicine_category
       medicine.medicine_type = medicine_type
       medicine.description = description
       medicine.price = price
       medicine.featured_image = featured_image
       medicine.stock_quantity = 80
       #medicine.medicine_id = generate_random_medicine_ID()
       
       medicine.save()
       
       return redirect('medicine-list')
   
    return render(request, 'hospital_admin/add-medicine.html',{'admin': user})
```

## Medicine Table
![title](pharmacist /Screenshot (244).png)

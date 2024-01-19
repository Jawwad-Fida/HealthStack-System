# HealthStack-System

- An online platform that caters to multiple hospitals, enabling efficient tracking, monitoring, and sharing of patient health records between themselves. Patients can access information on various hospitals and doctors, book appointments online, purchase medicines from an online pharmacy, pay for laboratory tests via an integrated payment gateway, and even chat with their appointed doctors.
- Software Engineering Project - B.Sc. in Computer Science and Engineering (CSE)

## Contributors

- **Team Members:** [Mohammed Jawwadul Islam](https://www.linkedin.com/in/jawwadfida/), [Mohammad Fahad Al Rafi](https://www.linkedin.com/in/md-fahad-al-al-rafi-14b968111/), [Moumy Kabir](https://www.linkedin.com/in/pranto-podder-b78b97162/), [Pranto Podder](https://www.linkedin.com/in/aysha-siddika-577ba5224/), [Aysha Siddika](https://www.linkedin.com/in/moumy-kabir-156a0a232/), Nafisa Akhter
- **Project Duration:** August 2022 - September 2022

## Tools used:
      1) Programming Language and Libraries: Django (Python web framework), Bootstrap, JavaScript, Ajax, Django REST framework.
      2) Database: SQLite
      3) APIs used: MailTrap, SSLCommerz Payment Gateway, , Django PDF library, Django channels for chat, ngrok HTTP, PyPI packages.

## Features

- **Users:** Patient, Doctor, Hospital Admin, Lab Worker, Pharmacist

### Patient
      1)  Search multiple Hospital → Department List → Search for Doctors
      2)  Doctor Profile → Book Appointment
      3)  Pay Appointment + Mail Confirmation 
      4)  Search all Doctors in all hospitals
      5)  Chat with appointed Doctor
      6)  View Prescription, Download Prescription (PDF)
      7)  Choose which tests to pay (Cart System, payment + mail confirmation)
      8)  View Report, Download Report (PDF)
      9)  Give Doctor Review
      10) Search for Medicines in Medical Shop (Pharmacy)
      11) Select which medicines to purchase (Cart system), pay total amount for medicines (payment + mail confirmation)
      
### Doctor 
      1)  Doctor Profile Settings (Add More feature)
      2)  Search multiple Hospital → Doctor register to hospital + upload certificate
      3)  (Once registered by admin) accept or reject patients appointment (mail confirmation send to patient)
      4)  Search patient profile → Create and view Prescription, view report
      5)  Chat with appointed Patient
      
### Hospital Admin
      1)  Admin Dashboard
      2)  Accept or reject doctor registration (view doctor profile to see details)
      3)  CRUD Hospitals (Add more)
      4)  View Hospital List → CRUD Departments within hospital
      5)  CRUD Lab Worker
      6)  CRUD Pharmacist

### Lab worker
      1)  Lab Worker Dashboard
      2)  Create Report for patient.
      3)  Create Tests for hospitals, View Tests

### Pharmacist
      1)  Pharmacist Dashboard
      2)  CRUD Medicines
      3)  Search Medicine


## APIs and PyPI packages used:

#### [Django Rest Framework](https://www.django-rest-framework.org/#installation) - toolkit for building web APIs
#### [Django Widget Tweaks](https://pypi.org/project/django-widget-tweaks/) - tweak form field rendering in templates
#### [Pillow](https://pillow.readthedocs.io/en/stable/index.html) - Python imaging library
#### [Mailtrap API](https://mailtrap.io/blog/django-send-email/) - smtp fake testing server
#### [Django Environ](https://django-environ.readthedocs.io/en/latest/) - protecting credentials online (.env file)
#### [SSLCommerz API](https://github.com/sslcommerz/SSLCommerz-Python) - a payment gateway that provides various payment options in Bangladesh (debit card, credit card, mobile banking, etc.)
#### [Django Debug Toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/installation.html) - configurable set of panels that display various debug information about the current request/response and when clicked
#### [xhtml2pdf](https://xhtml2pdf.readthedocs.io/en/latest/usage.html) - to generate and download pdf documents.

## Installation Details
      1) Create an environment to run django project  
      2) Migrate to create dbsqlite database 
      3) Look for .env.example and settings.py files to see what credentials to set up, and then create .env files
      
      The credentials that you need to set up are: Mailtrap credentials, SSLCommerz Credentials. 

## Steps to start the app
      1) Start python virtual env
            python -m venv venv
      2) Activate the virtual environment venv
            source venv/bin/activate
      3) Install python pip paclages
            pip install -r requirements
      4) Create .env from  .env.example and add secret key
            cp .env.example .env
      5) Upgrade django framework
            pip install --upgrade djangorestframework-simplejwt
      6) Migrate DB 
            python manage.py migrate
      7) Start the application
            python manage.py runserver
            

# MKDocs Documentation, Youtube Video and Presentation
- [Youtube](https://youtu.be/TSR00OKBSCY) video link of MKDocs documentation on our Healthstack project.
- [HeathStack Software - Presentation](https://github.com/Jawwad-Fida/HealthStack-System/files/13839586/HeathStack.Software.-.Presentation.pdf)
- Checkout out the [MKdocs documentation](https://jawwad-fida.github.io/HealthStack-System/) to see screenshots of our project.

# Some Screenshots

## Home page

<img src="https://user-images.githubusercontent.com/64092765/191188204-39dc320f-ec0f-4634-a8db-4735fd89cec9.png" width="50%">

<img src="https://user-images.githubusercontent.com/64092765/191188212-a48d1616-42ec-4413-bb7f-cf0d6347b165.png" width="50%">

<img src="https://user-images.githubusercontent.com/64092765/191188230-2a57e567-a879-487f-a907-8e6add15c8ca.png" width="50%">


## Patient

<img src="https://user-images.githubusercontent.com/64092765/191187372-0ea1bc75-aeee-4d2a-8624-27877d213753.png" width="50%">

<img src="https://user-images.githubusercontent.com/64092765/191187384-46f21266-3550-42a9-b3c9-17b19e870608.png" width="50%">

<img src="https://user-images.githubusercontent.com/64092765/191187390-b5dd8bbb-b7e6-4ba6-9423-71e93332e020.png" width="50%">

<img src="https://user-images.githubusercontent.com/64092765/191187405-73b06afa-10ac-46b2-9138-8eb077401d5b.png" width="50%">

<img src="https://user-images.githubusercontent.com/64092765/191187428-1445ca78-626d-4b00-8bc6-ce8639f2c303.png" width="50%">

<img src="https://user-images.githubusercontent.com/64092765/191187437-e415ed6b-cddc-4862-b34c-6ce59a75c72d.png" width="50%">

## Doctor

<img src="https://user-images.githubusercontent.com/64092765/191187476-aae75261-0298-4d13-bc19-d2db8918c1f6.png" width="50%">

<img src="https://user-images.githubusercontent.com/64092765/191187496-f1e0e7e4-ecd4-4c5d-8fdf-abc77a7d2031.png" width="50%">

<img src="https://user-images.githubusercontent.com/64092765/191187508-d03649a8-00ba-4c4c-a4a5-8a17a6fa196f.png" width="50%">

## Hospital Admin

<img src="https://user-images.githubusercontent.com/64092765/191187604-4985a19c-c292-47a9-a21b-befd03500dae.png" width="50%">

<img src="https://user-images.githubusercontent.com/64092765/191187692-05edf07b-a94f-4723-9e95-6b5c04cf03d8.png" width="50%">

<img src="https://user-images.githubusercontent.com/64092765/191187722-820d572b-2a20-4fd1-bc5b-70af699c43b7.png" width="50%">

## Pharmacist and Pharmacy

<img src="https://user-images.githubusercontent.com/64092765/191187822-6468adf2-c3ca-470a-87e7-1360e5415435.png" width="50%">

<img src="https://user-images.githubusercontent.com/64092765/191187869-24175b0d-38b2-41ff-9eb7-c793b8af0aa1.png" width="50%">

<img src="https://user-images.githubusercontent.com/64092765/191187883-dfd52812-b521-467d-9094-d5ff75f36492.png" width="50%">

<img src="https://user-images.githubusercontent.com/64092765/191187934-cfec116d-9a4d-420a-8270-6edab947ba95.png" width="50%">

### Lab Worker

<img src="https://user-images.githubusercontent.com/64092765/191188113-f9bb37ae-30a2-46b3-a871-e3ca5aa3df47.png" width="50%">

<img src="https://user-images.githubusercontent.com/64092765/191188138-2dd284c8-a815-4060-87f3-61ffd7c2300d.png" width="50%">


# [Champion in UIU CSE Project Show Summer 2022 - Software Engineering Laboratory](https://www.facebook.com/100080783675315/posts/pfbid0TuQyeVT9LHJx4zCnCpaDsAGFnCGxSTMKa8Fd1XCNcpf3n1yXf6ceQQTYQ1DeahSZl/)

<img src="https://user-images.githubusercontent.com/64092765/192018455-de998881-ac7e-4082-a8c6-3a36a59aef94.jpg" width="75%">

<img src="https://user-images.githubusercontent.com/64092765/191054866-189bb76f-3377-440a-84be-d07578a26c35.jpg" width="50%">






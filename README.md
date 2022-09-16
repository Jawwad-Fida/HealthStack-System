# HealthStack-System

- An online based platform for multiple hospitals. Provide immediate medical assistance to patients who require emergency treatment. Ability to track, monitor, and share a patient's health records between all hospitals. Patients can also see information regarding multiple hospitals and doctors, as well as take appointments via online.
- Software Engineering Project - B.Sc. in Computer Science and Engineering (CSE)
- Django Application

## Contributors

- **Team Members:** [Mohammed Jawwadul Islam](https://www.linkedin.com/in/jawwadfida/), [Mohammad Fahad Al Rafi](https://www.linkedin.com/in/md-fahad-al-al-rafi-14b968111/), [Moumy Kabir](https://www.linkedin.com/in/pranto-podder-b78b97162/), [Pranto Podder](https://www.linkedin.com/in/aysha-siddika-577ba5224/), [Aysha Siddika](https://www.linkedin.com/in/moumy-kabir-156a0a232/), Nafisa Akhter
- **Project Duration:** August 2022 - September 2022


## Tools used:
      1) **Front-end:** HTML, CSS, Boostrap, Javascript
      2) **Back-end:** Django (Python web framework)
      3) **Database:** SQLite
      4) **Others:** Various APIs, PyPI packages, Ajax 

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




## Installation Details
      After downloading project: - 
      1)Install PHPMAILER by running : - composer require phpmailer/phpmailer (in project folder) (Refer to github link below in Credits).
      2)Install PHP dotenv by running: - composer require vlucas/phpdotenv (in project folder) (Refer to github link below in Credits).
      3)Install PHP mPDF library by running: - composer composer require mpdf/mpdf (in project folder) (Refer to github link below in Credits).
      3)Create account in [Mailtrap](https://mailtrap.io/) and take your account credentials.
      4)Set up the database - radon.sql
      5)Register a user and then change user_role to Admin in order to view Admin Privileges.
      6)For Payment Gateway --> SSLCOMMERZ was used (Largest payment gateway in Bangladesh) (Refer to github link below in Credits). Payment Gateway has credentials.   
      7)Look for .env.example files in the directories to see what credentials to set up, and then create .env files in those directories. 
      
      The credentials that you need to set up are: Mailtrap credentials, SSLCommerz Credentials. 
       

### API's and Composer packages used: -
      phpmailer package and mailtrap API - smtp fake testing server
      PHP dotenv package - protecting credentials online (creating .env file)
      SSLCommerz API - a payment gateway that provides various payment options in Bangladesh (debit card, credit card, mobile banking, etc.)
      PHP mPDF library - to generate and download pdf documents. 
      
## Project video link - [Youtube](#)

## Credits

### 1) [PHPMailer and MailTrap](https://github.com/PHPMailer/PHPMailer)

PHPMailer resources are provided by [SmartMessages](https://info.smartmessages.net/)

### 2) [PHP dotenv](https://github.com/vlucas/phpdotenv) 

PHP dotenv was created by [Vance Lucas](https://github.com/vlucas) and [Graham Campbell](https://twitter.com/GrahamJCampbell)

### 3) [SSLCOMMERZ](https://www.sslcommerz.com/) payment gateway.

 * https://github.com/sslcommerz

### 4) [PHP mPDF library](https://github.com/sslcommerz)

## Screenshots 

from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from hospital.models import User, Hospital_Information
from .models import Admin_Information, Clinical_Laboratory_Technician

class AdminUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    # create a style for model form
    def __init__(self, *args, **kwargs):
        super(AdminUserCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
            

class LabWorkerCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    # create a style for model form
    def __init__(self, *args, **kwargs):
        super(LabWorkerCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

class PharmacistCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    # create a style for model form
    def __init__(self, *args, **kwargs):
        super(PharmacistCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

# class EditLabWorkerForm(forms.ModelForm):
#     class Meta:
#         model = Clinical_Laboratory_Technician
#         fields = ['name', 'age', 'phone_number', 'featured_image']

#     def __init__(self, *args, **kwargs):
#         super(EditLabWorkerForm, self).__init__(*args, **kwargs)

#         for name, field in self.fields.items():
#             field.widget.attrs.update({'class': 'form-control'})



class AddHospitalForm(ModelForm):
    class Meta:
        model = Hospital_Information
        fields = ['name','address','featured_image','phone_number','email','hospital_type']

    def __init__(self, *args, **kwargs):
        super(AddHospitalForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

class EditHospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital_Information
        fields = ['name','address','featured_image','phone_number','email','hospital_type']

    def __init__(self, *args, **kwargs):
        super(EditHospitalForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class EditEmergencyForm(forms.ModelForm):
    class Meta:
        model = Hospital_Information
        fields = ['general_bed_no','available_icu_no','regular_cabin_no','emergency_cabin_no','vip_cabin_no']

    def __init__(self, *args, **kwargs):
        super(EditEmergencyForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

class AddEmergencyForm(ModelForm):
    class Meta:
        model = Hospital_Information
        fields = ['name','general_bed_no','available_icu_no','regular_cabin_no','emergency_cabin_no','vip_cabin_no']

    def __init__(self, *args, **kwargs):
        super(AddEmergencyForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})



class AdminForm(ModelForm):
    class Meta:
        model = Admin_Information
        fields = ['name', 'email', 'phone_number', 'role','featured_image']

    def __init__(self, *args, **kwargs):
         super(AdminForm, self).__init__(*args, **kwargs)

         for name, field in self.fields.items():
             field.widget.attrs.update({'class': 'form-control'})


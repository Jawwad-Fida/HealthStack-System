from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from hospital.models import User
from .models import Admin_Information

class AdminUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    # create a style for model form
    def __init__(self, *args, **kwargs):
        super(AdminUserCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


# class AdminForm(ModelForm):
#     class Meta:
#         model = Admin_Information
#         fields = ['name', 'email', 'phone_number', 'role']

#     def __init__(self, *args, **kwargs):
#         super(AdminForm, self).__init__(*args, **kwargs)

#         for name, field in self.fields.items():
#             field.widget.attrs.update({'class': 'form-control'})
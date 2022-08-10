from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from hospital.models import User
from .models import Doctor_Information

# # Create a custom form that inherits from user form (reason --> for modify and customize)


class DoctorUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        # password1 and password2 are required fields (django default)
        fields = ['username', 'email', 'password1', 'password2']
        # labels = {
        #     'first_name': 'Name',
        # }

    # create a style for model form
    def __init__(self, *args, **kwargs):
        super(DoctorUserCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control floating'})

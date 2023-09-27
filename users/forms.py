from django import forms
from django.contrib.auth.models import User
from .models import Location, Profile
from localflavor.us.forms import USZipCodeField
from .widgets import CustomPhotoWidget


class UserForm(forms.ModelForm):
    username = forms.CharField(disabled=True)
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')


class ProfileForm(forms.ModelForm):
    photo = forms.ImageField(widget=CustomPhotoWidget)
    bio = forms.TextInput()
    class Meta:
        model = Profile
        fields = ('photo', 'bio', 'phone_number')
    


class LocationForm(forms.ModelForm):

    zip_code = USZipCodeField(required=True)

    class Meta:
        model = Location
        fields = {
            'address_1', 'address_2', 'city', 'state',
            'zip_code'
        }
from django import forms
from .models import Listing
from django.contrib.auth.models import User

from .models import Location, Profile, Bid
# from .widgets import CustomPictureImageFieldWidget

class UserForm(forms.ModelForm):
    username = forms.CharField(disabled=True)
    class Meta:
        model = User
        fields = {'username', 'first_name', 'last_name', 'email'}

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = {'photo', 'bio', 'phone_number'}

class ListingForm(forms.ModelForm):

    class Meta:
        model = Listing
        fields = {'brand', 'model', 'vin', 'mileage','color', 'description', 'engine', 'transmission', 'image'}

class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ['amount']

        
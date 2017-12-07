from django import forms
from .models import *
from django.forms import widgets


class CarRideForm(forms.Form):
    your_name = forms.CharField(label='First Name', max_length=30)
    email = forms.EmailField(label='Email')


# class NewProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ('picture', 'bio', 'work')
#         widgets = {
#             'profile': forms.CheckboxSelectMultiple(),
#         }


class VehicleAddForm(forms.ModelForm):
    make = forms.CharField(widget=forms.TextInput(
        attrs={'required': True, 'class': 'form-control'}))
    model = forms.CharField(widget=forms.TextInput(
        attrs={'required': True, 'class': 'form-control'}))

    type = forms.ChoiceField(choices=(('private', 'private'), ('hired', 'hired')),
                             widget=forms.Select(attrs={'class': 'form-control', 'required': True}))
    seats = forms.IntegerField(widget=forms.TextInput(
        attrs={'type': 'number', 'class': 'form-control', 'required': True}))


class Meta:
    model = Vehicle
    fields = ['make', 'model', 'plate', 'seats', 'type']


class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        exclude = ['user', ]
        fields = ('driver', 'liscence_no', 'scanned', 'car_picture',
                  'number_plates', 'capacity', 'color', 'phone', 'city')


class PassengerForm(forms.ModelForm):
    class Meta:
        model = Passenger
        exclude = ['user', ]
        fields = ('passenger', 'scanned', 'confirmed')

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(PassengerForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.instance.user = self.user
        super(PassengerForm, self).save(*args, **kwargs)

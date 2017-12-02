from django import forms
from .models import Profile


class CarRideForm(forms.Form):
    your_name = forms.CharField(label='First Name', max_length=30)
    email = forms.EmailField(label='Email')


class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['picture', 'bio', 'work']
        widgets = {
            'profile': forms.CheckboxSelectMultiple(),
        }

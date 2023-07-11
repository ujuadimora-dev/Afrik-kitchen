from django import forms
from django.core.validators import EmailValidator


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.CharField(validators=[EmailValidator()])
    phone = forms.CharField(max_length=15)
    choice_of_event = forms.CharField(max_length=100)
    number_of_guest = forms.CharField(max_length=100)
    other_info = forms.CharField(widget=forms.Textarea)
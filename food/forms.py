from django import forms
from django.forms import fields
from .models import MenuItem


class MenuitemDetail(forms.ModelForm):
    class Meta:
        model=MenuItem
        fields="__all__"
from django import forms
from .models import * 
class RegisterForms(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields ='__all__'



from django import forms
from .models import Item, Owner
from django.contrib.auth.forms import AuthenticationForm

class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('name', 'code', 'description',)

class OwnerForm(forms.ModelForm):

    class Meta:
        model = Owner
        fields = ('item', 'codeItem', 'nickname',)

class UserLogin(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
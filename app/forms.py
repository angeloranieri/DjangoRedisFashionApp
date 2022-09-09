from django import forms

from .models import Item, Owner

class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('name', 'description',)

class OwnerForm(forms.ModelForm):

    class Meta:
        model = Owner
        fields = ('item', 'codeItem', 'nickname',)
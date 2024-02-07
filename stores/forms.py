from django.forms import ModelForm
from django import forms
from stores.models import Products


class Add_productForms(ModelForm):
    class Meta:
        model = Products
        fields = ('name', 'image', 'price', 'category', 'description', 'owner')
        labels = {
            'name': '',
            'image': '',
            'price': '',
            'category': '',
            'description': '',
        }
        
        #styling form
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type name of product here'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insert price of product'}),
            'category': forms.Select(attrs={'class': 'form-control', 'placeholder': '-- Choose Category --'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Add product description'}),
        }
        
        
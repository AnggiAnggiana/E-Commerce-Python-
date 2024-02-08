from django.forms import ModelForm
from django import forms
from stores.models import Products, Customers


class ProductForms(ModelForm):
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
        
class ProfileForms(ModelForm):
    class Meta:
        model = Customers
        fields = ('owner_id', 'image', 'first_name', 'last_name', 'email', 'password', 'phone_number', 'address', 'gender')
        labels = {
            'image': '',
            'first_name': '',
            'last_name': '',
            'email': '',
            'password': '',
            'phone_number': '',
            'address': '',
            'gender': '',
        }
        
        # Styling form
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control'}),
        }
        
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect())

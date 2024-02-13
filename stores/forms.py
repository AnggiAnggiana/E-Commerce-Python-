from django.forms import ModelForm
from django import forms
from stores.models import Products, Customers, Sellers
from django.forms.widgets import SelectDateWidget


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
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insert price of product(numbers)'}),
            'category': forms.Select(attrs={'class': 'form-control', 'placeholder': '-- Choose Category --'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Add product description'}),
        }
        
class ProfileForms(ModelForm):
    class Meta:
        model = Customers
        fields = ('owner_id', 'image', 'first_name', 'last_name', 'email', 'birthdate', 'phone_number', 'address', 'gender')
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
    
    birthdate = forms.DateField(
        widget=SelectDateWidget(years=range(1900, 2101), attrs={'class': 'birthdate-select'})
    )


class SellerForms(ModelForm):
    class Meta:
        model = Sellers
        fields = ('owner_id', 'store_name', 'email', 'birthdate', 'phone_number', 'address', 'image', 'gender')
        labels = {
            'store_name': '',
            'email': '',
            'birthdate': '',
            'phone_number': '',
            'address': '',
            'image': '',
            'gender': '',
        }
        
        # Styling Form
        widgets = {
            'store_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control'}),
        }
        
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect())
    
    birthdate = forms.DateField(
        widget=SelectDateWidget(years=range(1900, 2101), attrs={'class': 'birthdate-select'})
    )
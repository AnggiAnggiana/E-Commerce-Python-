from django.forms import ModelForm
from django import forms
from stores.models import Products, Customers, Sellers, Smartphone, Foods, Comment_Smartphone, Comment_Foods
from django.forms.widgets import SelectDateWidget


class ProductForms(ModelForm):
    class Meta:
        model = Products
        fields = ('categories',)
        labels = {
            'categories': '',
        }

        # Styling Form
        widgets = {
            'categories': forms.Select(attrs={'class': 'form-control', 'placeholder': '-- Choose Condition --'}),
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
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email address'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+62 85xxxxx'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your address'}),
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
            'store_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Store Name'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'example123@email.com'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+62 85xxxxx'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Store Address'}),
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
    
class SmartphoneForms(ModelForm):
    class Meta:
        model = Smartphone
        fields = ('name', 'categories', 'price', 'image', 'memory_capacity', 'ram_capacity', 'warranty_period', 'stock', 'seller_Address', 'condition', 'brand', 'owner', 'description')
        labels = {
            'name': '',
            'categories': '',
            'price': '',
            'image': '',
            'memory_capacity': '',
            'ram_capacity': '',
            'warranty_period': '',
            'stock': '',
            'seller_Address': '',
            'condition': '',
            'brand': '',
            'owner': '',
            'description': '',
        }
        
        #Styling Form
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product Name'}),
            'categories': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select Categories', 'readonly': 'readonly'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type Product Price (Numbers) e.g 1000000'}),
            'memory_capacity': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '120GB'}),
            'ram_capacity': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '10GB'}),
            'warranty_period': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '2 years'}),
            'stock': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '100'}),
            'seller_Address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sent From (Type the Address here)'}),
            'condition': forms.Select(attrs={'class': 'form-control', 'placeholder': '-- Choose Condition --'}),
            'brand': forms.Select(attrs={'class': 'form-control', 'placeholder': '-- Choose Brand --'}),
            'owner': forms.Select(attrs={'class': 'form-control', 'placeholder': '-- Choose Owner --', 'readonly': 'readonly'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Product Description'}),
        }
        
class FoodForms(ModelForm):
    class Meta:
        model = Foods
        fields = ('food_name', 'food_categories', 'food_price', 'food_image', 'storage_period', 'storage_condition', 'product_weight', 'number_product', 'food_stock', 'food_description', 'food_seller_Address', 'food_owner')
        labels = {
            'food_name': '',
            'food_categories': '',
            'food_price': '',
            'food_image': '',
            'storage_period': '',
            'storage_condition': '',
            'product_weight': '',
            'number_product': '',
            'food_stock': '',
            'food_description': '',
            'food_seller_Address': '',
            'food_owner': '',
        }
        
        #Styling Form
        widgets = {
            'food_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product Name'}),
            'food_categories': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select Categories', 'readonly': 'readonly'}),
            'food_price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type Product Price (Numbers) e.g 500000'}),
            'storage_period': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '1 bulan'}),
            'storage_condition': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Beku (0°C)'}),
            'product_weight': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '500gram'}),
            'number_product': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '1 Pack (5pcs)'}),
            'food_stock': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '400'}),
            'food_description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Product Description'}),
            'food_seller_Address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sent From (Type the Address here)'}),
            'food_owner': forms.Select(attrs={'class': 'form-control', 'placeholder': '-- Choose Owner --', 'readonly': 'readonly'}),
        }
        
class Comment_SmartphoneForm(forms.ModelForm):
    # pictures = forms.FileField(required=False, widget=MultipleFileInput(attrs={"multiple": True}))
    
    class Meta:
        model = Comment_Smartphone
        fields = ('user', 'smartphone', 'text', 'pictures')
        label = {
            'user': '',
            'smartphone': '',
            'text': '',
            'pictures': '',
        }
        
        #Styling Form
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}),
            'smartphone': forms.Select(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Type your review here'}),
        }
    
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['pictures'].widget.attrs["accept"] = ".jpg, .jpeg, .png"
        
# CommentPictureFormSet = forms.inlineformset_factory(Smartphone, Comment_Smartphone, fields=('pictures',), extra=6)

class Comment_FoodForm(forms.ModelForm):
    class Meta:
        model = Comment_Foods
        fields = ('user', 'food', 'text', 'pictures')
        label = {
            'user': '',
            'food': '',
            'text': '',
            'pictures': '',
        }
        
        #Styling Form
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}),
            'food': forms.Select(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Type your review here'}),
        }
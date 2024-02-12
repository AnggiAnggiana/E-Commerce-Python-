from django.db import models
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    activation_key = models.CharField(max_length=255, unique=True)
    email_validated = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username
    
@receiver(post_save, sender=User, dispatch_uid="save_new_user_profile")
def save_profile(sender, instance, created, **kwargs):
    user = instance
    if created:
        profile = Profile.objects.create(user=user)
        profile.save()
        

class Customers(models.Model):
    owner_id = models.IntegerField(blank=True, default=1)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=60)
    birthdate = models.DateField(default=None, blank=True, null=True)
    phone_number = models.CharField(max_length=30)
    address =  models.TextField(max_length=150)
    image = models.ImageField(upload_to='uploads/customers', default='')
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    
    gender = models.CharField(max_length=30, choices=GENDER_CHOICES, default='')
    
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    class Meta:
        verbose_name_plural = 'Customers'

    
class Sellers(models.Model):
    owner_id = models.IntegerField(blank=True, default=1)
    store_name = models.CharField(max_length=50, default='')
    email = models.EmailField(max_length=60)
    birthdate = models.DateField(default=None, blank=True, null=True)
    phone_number = models.CharField(max_length=20)
    address =  models.TextField(max_length=150)
    image = models.ImageField(upload_to='uploads/sellers', default='')
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    
    gender = models.CharField(max_length=30, choices=GENDER_CHOICES, default='')
    
    def __str__(self):
        return self.store_name
    
    class Meta:
        verbose_name_plural = 'Sellers'

class Categories(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categories'
    
class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    description = models.TextField(max_length=300, blank=True, null=True)
    image = models.ImageField(upload_to='uploads/product')
    owner = models.ForeignKey(Sellers, on_delete=models.CASCADE, default='')
    
    def __str__(self):
        return self.name
    
    # Put (.) after 3 numbers from behind
    def formatted_price(self):
        return '{:,.0f}'.format(self.price).replace(',','.')
    
    class Meta:
        verbose_name_plural = 'Products'

class Transactions(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    phone = models.CharField(max_length=30, blank=True, null=True)
    address = models.TextField(max_length=150, blank=True, null=True)
    quantity = models.IntegerField(default=1)
    date = models.DateField(default=datetime.datetime.today)
    transaction_status = models.BooleanField(default=False)
    
    def __str__(self):
        return self.product
    
    class Meta:
        verbose_name_plural = 'Transactions'

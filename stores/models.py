from django.db import models
import datetime

class Customers(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=60)
    password = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    address =  models.TextField(max_length=150)
    image = models.ImageField(upload_to='uploads/customers', default='')
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    class Meta:
        verbose_name_plural = 'Customers'
    
class Sellers(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=60)
    password = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=20)
    address =  models.TextField(max_length=150)
    image = models.ImageField(upload_to='uploads/sellers', default='')
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
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

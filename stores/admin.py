from django.contrib import admin
from stores.models import Customers, Sellers, Products, Transactions, Smartphone, Foods

class CustomersDisplay(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'birthdate', 'gender', 'address')
    
class SellersDisplay(admin.ModelAdmin):
    list_display = ('store_name', 'email', 'birthdate', 'phone_number', 'address', 'gender')

class SmartphoneDisplay(admin.ModelAdmin):
    list_display = ('name', 'categories', 'price', 'memory_capacity', 'ram_capacity', 'warranty_period', 'stock', 'seller_Address', 'condition', 'brand', 'owner')

class FoodsDisplay(admin.ModelAdmin):
    list_display = ('food_name', 'food_categories', 'food_price', 'food_stock', 'storage_period', 'storage_condition', 'product_weight', 'number_product', 'food_seller_Address', 'food_owner')

admin.site.register(Customers, CustomersDisplay)
admin.site.register(Sellers, SellersDisplay)
admin.site.register(Products)
admin.site.register(Transactions)
admin.site.register(Smartphone, SmartphoneDisplay)
admin.site.register(Foods, FoodsDisplay)
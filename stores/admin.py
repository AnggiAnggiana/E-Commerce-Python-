from django.contrib import admin
from stores.models import Customers, Sellers, Products, Transactions, Smartphone, Foods, Comment_Smartphone, Shopping_Cart, Profile

class ProfileDisplay(admin.ModelAdmin):
    list_display = ('user', 'activation_key', 'email_validated')

class CustomersDisplay(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'birthdate', 'street', 'district', 'city', 'province', 'country', 'gender')
    
class SellersDisplay(admin.ModelAdmin):
    list_display = ('store_name', 'email', 'birthdate', 'phone_number', 'street', 'district', 'city', 'province', 'country', 'gender')

class SmartphoneDisplay(admin.ModelAdmin):
    list_display = ('name', 'categories', 'price', 'memory_capacity', 'ram_capacity', 'warranty_period', 'stock', 'seller_Address', 'condition', 'brand', 'owner')

class FoodsDisplay(admin.ModelAdmin):
    list_display = ('food_name', 'food_categories', 'food_price', 'food_stock', 'storage_period', 'storage_condition', 'product_weight', 'number_product', 'food_seller_Address', 'food_owner')

class Comment_SmartphoneDisplay(admin.ModelAdmin):
    list_display = ('user', 'smartphone', 'text', 'created_at')

class Shopping_CartDisplay(admin.ModelAdmin):
    list_display = ('user', 'product_smartphone', 'product_food', 'quantity', 'total_price')


admin.site.register(Profile, ProfileDisplay)
admin.site.register(Customers, CustomersDisplay)
admin.site.register(Sellers, SellersDisplay)
admin.site.register(Products)
admin.site.register(Transactions)
admin.site.register(Smartphone, SmartphoneDisplay)
admin.site.register(Foods, FoodsDisplay)
admin.site.register(Comment_Smartphone, Comment_SmartphoneDisplay)
admin.site.register(Shopping_Cart, Shopping_CartDisplay)
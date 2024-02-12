from django.contrib import admin
from stores.models import Customers, Sellers, Categories, Products, Transactions

class CustomersDisplay(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'birthdate', 'gender', 'address')


admin.site.register(Customers, CustomersDisplay)
admin.site.register(Sellers)
admin.site.register(Categories)
admin.site.register(Products)
admin.site.register(Transactions)
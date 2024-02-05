from django.contrib import admin
from stores.models import Customers, Sellers, Categories, Products, Transactions

admin.site.register(Customers)
admin.site.register(Sellers)
admin.site.register(Categories)
admin.site.register(Products)
admin.site.register(Transactions)
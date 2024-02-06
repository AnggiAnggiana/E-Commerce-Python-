from . import views
from django.urls import path

urlpatterns  = [
    path('', views.homepage, name='homepage'),
    path('products/<product_id>', views.product_show, name='product_show'),
]
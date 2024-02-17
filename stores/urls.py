from . import views
from django.urls import path

urlpatterns  = [
    path('', views.homepage, name='homepage'),
    path('products/smartphone/<smartphone_id>', views.smartphone_show, name='smartphone_show'),
    path('add_product/', views.add_product, name='add_product'),
    path('edit_product_smartphone/<smartphone_id>', views.edit_product_smartphone, name='edit_product_smartphone'),
    path('completed_customer_profile/', views.add_customer_profile, name='add_customer_profile'),
    path('user/account/profile', views.customerProfile, name='customerProfile'),
    path('add_seller_profile', views.add_seller_profile, name='add_seller_profile'),
]
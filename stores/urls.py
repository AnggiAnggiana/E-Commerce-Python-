from . import views
from django.urls import path

urlpatterns  = [
    path('', views.homepage, name='homepage'),
    path('products/smartphone/<smartphone_id>', views.smartphone_show, name='smartphone_show'),
    path('products/food/<food_id>', views.food_show, name='food_show'),
    path('add_product/', views.add_product, name='add_product'),
    path('edit_product_smartphone/<smartphone_id>', views.edit_product_smartphone, name='edit_product_smartphone'),
    path('edit_product_food/<food_id>', views.edit_product_food, name='edit_product_food'),
    path('completed_customer_profile/', views.add_customer_profile, name='add_customer_profile'),
    path('user/account/profile', views.customerProfile, name='customerProfile'),
    path('add_seller_profile', views.add_seller_profile, name='add_seller_profile'),
    path('search_result/', views.search_results, name='search_results'),
    path('store/<store_name>', views.seller_store, name='seller_store'),
    path('cart/', views.cart_shop, name='cart_shop'),
    path('cart/delete/<int:item_id>/', views.delete_cart_item, name='delete_cart_item'),
    path('checkout/', views.checkout_product, name='checkout_product'),
]
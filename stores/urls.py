from . import views
from django.urls import path

urlpatterns  = [
    path('', views.homepage, name='homepage'),
    path('products/<product_id>', views.product_show, name='product_show'),
    path('add_product/', views.add_product, name='add_product'),
    path('edit_product/<product_id>', views.edit_product, name='edit_product'),
    path('user/account/profile', views.user_profile, name='user_profile'),
]
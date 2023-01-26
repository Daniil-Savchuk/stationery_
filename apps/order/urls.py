from django.urls import path
from apps.order.views import add_to_cart, cart_page, create_order


urlpatterns = [
    path('add-to-cart/', add_to_cart, name='add_to_cart'),
    path('cart-page/', cart_page, name='cart_page'),
    path('create/', create_order, name='create_order'),
]

from django.urls import path
from apps.order.views import add_to_cart, cart_page


urlpatterns = [
    path('add-to-cart/', add_to_cart, name='add_to_cart'),
    path('cart-page/', cart_page, name='cart_page'),
]

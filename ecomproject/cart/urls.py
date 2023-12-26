from django.urls import path
from cart import views
app_name = 'cart'
urlpatterns = [
    path('add/<int:product_id>/',views.add_cart,name='add_cart'),
    path('cart/',views.cart_detail,name='cart_detail'),
    path('remove/<int:product_id>/',views.cart_remove,name='cart_remove'),
    path('delete/<int:product_id>/',views.cart_deletion,name='cart_deletion'),
]
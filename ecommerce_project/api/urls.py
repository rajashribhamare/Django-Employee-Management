from django.urls import path
from .views import (
    CartItemListCreateView,
    CartItemUpdateDeleteView,
    ClearCartView,
    TotalCartPriceView
)

urlpatterns = [
    path('cart/', CartItemListCreateView.as_view(), name='cart-list-create'),
    path('cart/<int:item_id>/', CartItemUpdateDeleteView.as_view(), name='cart-update-delete'),
    path('cart/clear/', ClearCartView.as_view(), name='cart-clear'),
    path('cart/total/', TotalCartPriceView.as_view(), name='cart-total'),
]

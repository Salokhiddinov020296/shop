from django.urls import path

from shop.views import ShopView, ProductDetailView

app_name = 'shop'
urlpatterns = [
        path('', ShopView.as_view(), name='shop'),
        path('product/<int:pk>/', ProductDetailView.as_view(), name='detail')
]
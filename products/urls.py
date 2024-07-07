from django.urls import path
from .views import ProductListView,productDetailView
urlpatterns = [
    path('',ProductListView.as_view(),name='products'),
    path('product_detail/<slug:slug>', productDetailView.as_view(), name='products_detail'),

]
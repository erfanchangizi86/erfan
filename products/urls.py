from django.urls import path
from .views import ProductListView
urlpatterns = [
    path('',ProductListView.as_view(),name='products'),
    path('product_detail/<slug:slug>', ProductListView.as_view(), name='products_detail'),

]
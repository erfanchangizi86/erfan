from django.shortcuts import render
from django.views.generic import ListView, DetailView

from products.models import Product


# Create your views here.


class ProductListView(ListView):
    model = Product
    template_name = 'product/product_list.html'
    context_object_name = 'products'

class productDetailView(DetailView):
    template_name = ''
    context_object_name = 'product'
    model = Product



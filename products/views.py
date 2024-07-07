from functools import wraps

from django.core.cache import cache
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView
from django.contrib.postgres.search import SearchVector
from products.models import Product, product_galry

from django.views.generic import ListView
from django.core.cache import cache

from utils.mixins import CacheListViewMixin


# Create your views here.

class ProductListView(ListView):
    model = Product
    template_name = 'product/product_list.html'
    context_object_name = 'products'
    ordering = ['-id']
    paginate_by = 4

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_active=True)
        # Product.objects.annotate(search=SearchVector('name', 'body','short_body')).filter(search="")
        return queryset


class productDetailView(CacheListViewMixin, DetailView):
    template_name = 'product/product_detail.html'
    context_object_name = 'product'
    model = Product

    def get_context_data(self, **kwargs):
        id_product = self.object.id
        context = super().get_context_data(**kwargs)
        context['gallery'] = product_galry.objects.filter(product_gallery_id=id_product, is_active=True,
                                                          is_deleted=False,)
        return context

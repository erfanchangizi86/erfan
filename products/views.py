from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView

from products.models import Product


# Create your views here.


class ProductListView(ListView):
    model = Product
    template_name = 'product/product_list.html'
    context_object_name = 'products'
    ordering = ['-id']
    paginate_by = 1

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_active=True, is_sale__iexact=Product.text_sale_choises.not_sale)
        return queryset


class productDetailView(DetailView):
    template_name = ''
    context_object_name = 'product'
    model = Product
    # @method_decorator()
    # def dispatch(self, request, *args, **kwargs):
    #     return super().dispatch(request,args,kwargs)

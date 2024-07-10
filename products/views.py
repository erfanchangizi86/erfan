from functools import wraps

from django.core.paginator import Paginator
from django.db.models import F

from .forms import BrandForm
from django.core.cache import cache
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView
from django.contrib.postgres.search import SearchVector
from products.models import Product, product_galry, category, Brands

from django.views.generic import ListView
from django.core.cache import cache
from django.views.decorators.http import require_http_methods
from utils.mixins import CacheListViewMixin


def get_subcategories(catego_ry):
    subcategories = catego_ry.children.all()
    subcategories_data = []

    for subcategory in subcategories:
        subcategories_data.append({
            'id': subcategory.id,
            'name': subcategory.title,
            'url_name': subcategory.url_name,
            'subcategories': get_subcategories(subcategory)
        })

    return subcategories_data


# Create your views here.

def get_all_categories():
    categories = category.objects.filter()  # دسته‌بندی‌های اصلی
    data = []
    for cate_gory in categories:
        data.append({
            'id': cate_gory.id,
            'name': cate_gory.title,
            'url_name': cate_gory.url_name,
            'subcategories': get_subcategories(cate_gory)
        })
    return data


class ProductListView(ListView):
    model = Product
    template_name = 'product/product_list.html'
    context_object_name = 'products'
    ordering = ['-id']
    paginate_by = 1

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_active=True)
        searches = self.request.GET.get('searches', '')
        if searches is not None and len(searches) > 0:
            queryset = Product.objects.annotate(search=SearchVector('name', 'short_body', 'body')).filter(
                search__contains=searches)
        categories = self.kwargs.get('cate_gory')
        if categories:
            queryset = queryset.filter(category_product__url_name__iexact=categories)

        self.forms = BrandForm(self.request.GET or None)
        if self.forms.is_valid():
            brandes = self.forms.cleaned_data['brand_name']
            queryset = queryset.filter(brand__in=brandes)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cate: category = category.objects.filter(is_active=True, is_deleted=False)
        context['categories'] = get_all_categories()
        context['brands'] = Brands.objects.filter(is_active=True).order_by('title_english')
        context['form'] = self.forms
        return context


class productDetailView(CacheListViewMixin, DetailView):
    template_name = 'product/product_detail.html'
    context_object_name = 'product'
    model = Product

    def get_context_data(self, **kwargs):
        id_product = self.object.id
        context = super().get_context_data(**kwargs)
        context['gallery'] = product_galry.objects.filter(product_gallery_id=id_product, is_active=True,
                                                          is_deleted=False, )
        return context


@require_http_methods(['GET', 'POST'])
def test(request):
    '''این دکاریتور برای اینکه نشان دهیم درخاست از چه نوعی است.'''


def listing(request):
    """
    صفحه بندی در فانکشن ها به این صورت است
    :param request:
    :return:
    """
    contact_list = Product.objects.filter(price__lt=F('sale_price')).order_by(F('price').desc(nulls_last=True))
    paginator = Paginator(contact_list, 25) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, '', {'page_obj': page_obj})
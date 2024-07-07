from django.shortcuts import render
from django.views.generic import TemplateView

from products.models import category


# Create your views here.


def header(request):
    categories: category = category.objects.filter(is_active=True,title_category__category=None).prefetch_related('category_set')
    context = {'categories': categories}
    return render(request,'shard/header.html',context)


def footer(request):
    context = {}
    return render(request,'shard/footer.html',context)
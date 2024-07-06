from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.


def header(request):
    context = {}
    return render(request,'shard/header.html',context)


def footer(request):
    context = {}
    return render(request,'shard/footer.html',context)
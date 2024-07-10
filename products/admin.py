from django.contrib import admin
from django import forms

from .models import Product, product_galry, category, Brands


# Register your models here.
@admin.register(Product)
class ModelNameAdmin(admin.ModelAdmin):
    pass


@admin.register(product_galry)
class admin_gallry(admin.ModelAdmin):
    pass


@admin.register(category)
class admin_category(admin.ModelAdmin):
    pass

class model_product(forms.ModelForm):
    def clean(self):
        title = self.cleaned_data.get('title')
        if title is None or title == '' or title == 'None':
            raise forms.ValidationError({'title':'Sorry, Title cant be None'})





@admin.register(Brands)
class BrandAdmin(admin.ModelAdmin):
    form = model_product
    list_display = ('title', 'title_english')
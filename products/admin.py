from django.contrib import admin

from .models import Product, product_galry, category


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

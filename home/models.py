from django.db import models

# Create your models here.
x = [
    {'id': 2, 'name': 'دیجیتال', 'subcategories': [{'id': 3, 'name': 'موبایل', 'subcategories': [{'id': 5, 'name': 'کاور موبایل', 'subcategories': []}]}
        , {'id': 4, 'name': 'لپتاپ', 'subcategories': []}]}
    , {'id': 3, 'name': 'موبایل', 'subcategories': [{'id': 5, 'name': 'کاور موبایل', 'subcategories': []}]},
    {'id': 4, 'name': 'لپتاپ', 'subcategories': []}, {'id': 5, 'name': 'کاور موبایل', 'subcategories': []}]
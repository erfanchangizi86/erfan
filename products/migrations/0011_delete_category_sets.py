# Generated by Django 5.0.6 on 2024-07-10 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_brands_product_brand'),
    ]

    operations = [
        migrations.DeleteModel(
            name='category_sets',
        ),
    ]
# Generated by Django 5.0.6 on 2024-07-07 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category_product',
            field=models.ManyToManyField(db_index=True, null=True, related_name='category_sets', to='products.category', verbose_name='دسته بندی'),
        ),
    ]

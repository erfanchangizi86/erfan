# Generated by Django 5.0.6 on 2024-07-08 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_category_sets_alter_category_title_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category_product',
            field=models.ManyToManyField(db_index=True, null=True, to='products.category', verbose_name='دسته بندی'),
        ),
    ]
# Generated by Django 5.0.6 on 2024-07-10 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, default='', max_length=200, unique=True, verbose_name='عنوان در url'),
        ),
    ]

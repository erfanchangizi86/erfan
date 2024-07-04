from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.

class Product(models.Model):
    class text_sale_choises(models.TextChoices):
        product_sale = "sale_product", 'محصول تخفیف دارد'
    name = models.CharField(max_length=100, db_index=True, verbose_name='عنوان')
    price = models.FloatField(verbose_name="قیمت")
    short_body = models.CharField(verbose_name="توضیحات کوتاه", max_length=300, db_index=True)
    body = models.TextField(db_index=True, verbose_name="توضیحات")
    is_active = models.BooleanField(default=True, verbose_name="فعال/غیرفعال")
    is_deleted = models.BooleanField(default=False, verbose_name="حذف شده/حذف نشده")
    # brans = models.ForeignKey(None, db_index=True, on_delete=models.CASCADE)
    # category_product = models.ManyToManyField(None, db_index=True)
    is_sale = models.CharField(db_index=True,max_length=300,choices=text_sale_choises.choices)
    sale_price = models.DecimalField(verbose_name="درصد تخفیف", default=0,max_digits=3, decimal_places=2)
    slug = models.SlugField()

    def __str__(self):
        return f"{self.name} ({self.price})"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("", kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'محصول '
        verbose_name_plural = 'محصولات '
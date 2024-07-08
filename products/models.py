from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class category_sets(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان")
    url_name = models.CharField(max_length=300, verbose_name="عنوان در url")
    is_active = models.BooleanField(default=True, verbose_name="فعال/غیرفعال")
    is_deleted = models.BooleanField(default=False, verbose_name="حذف شده/حذف نشده")

    def __str__(self):
        return f"{self.title}"


class category(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان")

    title_category = models.ForeignKey('category', on_delete=models.CASCADE, verbose_name="دسته بنده", null=True,
                                       blank=True, related_name='children')
    url_name = models.CharField(max_length=300, verbose_name="عنوان در url")
    is_active = models.BooleanField(default=True, verbose_name="فعال/غیرفعال")
    is_deleted = models.BooleanField(default=False, verbose_name="حذف شده/حذف نشده")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "دسته بنده ها"
        verbose_name_plural = "دسته بندی"

class Brands(models.Model):
    title = models.CharField(max_length=200,verbose_name='نام برند(به فارسی)')
    title_english = models.CharField(max_length=200,verbose_name="نام برند(به انگلیسی)")
    is_active = models.BooleanField(verbose_name='فعال/غیر فعال')
    url_name = models.CharField(max_length=400,verbose_name="عنوان در url(به انگلیسی)")
    def __str__(self):
        return f"{self.title}/{self.title_english}"

    class Meta:
        verbose_name = 'برندها'
        verbose_name_plural = 'برند'
# Create your models here.

class Product(models.Model):
    image = models.ImageField(upload_to="products/images")
    name = models.CharField(max_length=100, db_index=True, verbose_name='عنوان')
    price = models.FloatField(verbose_name="قیمت")
    short_body = models.CharField(verbose_name="توضیحات کوتاه", max_length=300, db_index=True)
    body = models.TextField(db_index=True, verbose_name="توضیحات")
    is_active = models.BooleanField(default=True, verbose_name="فعال/غیرفعال")
    is_deleted = models.BooleanField(default=False, verbose_name="حذف شده/حذف نشده")
    # brans = models.ForeignKey(None, db_index=True, on_delete=models.CASCADE)
    # category_product = models.ManyToManyField(None, db_index=True)
    is_sale = models.BooleanField(null=True, default=False, verbose_name="محصول تخفیف دارد./ندارد")
    sale_price = models.DecimalField(verbose_name="درصد تخفیف", default=0, max_digits=3, decimal_places=2)
    slug = models.SlugField(default='', null=False, blank=True, max_length=200, unique=True,
                            verbose_name='عنوان در url')
    category_product = models.ManyToManyField(category, verbose_name="دسته بندی",
                                              db_index=True, null=True)
    brand = models.ForeignKey(Brands, on_delete=models.CASCADE, verbose_name='برند', null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.price})"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("products_detail", args=[self.slug])

    class Meta:
        verbose_name = 'محصول '
        verbose_name_plural = 'محصولات '


class product_galry(models.Model):
    image = models.ImageField(upload_to="products/images/galry")
    product_gallery = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="گالری")
    is_active = models.BooleanField(default=True, verbose_name="فعال/غیرفعال")
    is_deleted = models.BooleanField(default=False, verbose_name="حذف شده/حذف نشده")

    def __str__(self):
        return f"{self.product_gallery}"

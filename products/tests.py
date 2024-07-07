from django.test import TestCase
from .models import product_galry, Product


# Create your tests here.
class ProductTestCase(TestCase):
    def test_setUp(self):
        prod = Product.objects.create(name='nokia')
        self.assertEqual(prod.name,"nokia")


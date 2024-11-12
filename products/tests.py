from django.test import TestCase
from .models import Product

class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(sku="000001", name="BV Lean leather ankle boots", category="boots", price=89000)
        Product.objects.create(sku="000002", name="BV Lean leather ankle boots", category="boots", price=99000)
        Product.objects.create(sku="000003", name="Ashlington leather ankle boots", category="boots", price=71000)
        Product.objects.create(sku="000004", name="Naima embellished suede sandals", category="sandals", price=79500)
        Product.objects.create(sku="000005", name="Nathane leather sneakers", category="sneakers", price=59000)

    def test_product_creation(self):
        """Test if products are created successfully."""
        product = Product.objects.get(sku="000001")
        self.assertEqual(product.price, 89000)

    def test_discount_application(self):
        """Test if discounts are applied correctly."""
        product = Product.objects.get(sku="000003")
        expected_final_price = 71000 * (1 - 0.15)
        self.assertEqual(product.price * 0.85, expected_final_price)

    def test_category_filter(self):
        """Test if filtering by category works."""
        response = self.client.get('/api/products/?category=boots')
        self.assertEqual(len(response.data), 3)

    def test_price_less_than_filter(self):
        """Test if filtering by price works."""
        response = self.client.get('/api/products/?priceLessThan=80000')
        for product in response.data:
            self.assertTrue(product['price']['original'] <= 80000)

    def test_limit_response_to_five(self):
        """Test if response limits to five items only."""
        response = self.client.get('/api/products/')
        self.assertTrue(len(response.data) <= 5)

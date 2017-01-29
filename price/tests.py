"""
Price tests module
"""
from django.test import Client
from django.test import TestCase
from django.core.urlresolvers import reverse
from price.models import Product


def insert_price():
    product_1 = Product.objects.create(name="A",
                                       price="1",
                                       discount_price="0.5",
                                       discount_number="2",
                                       discount_product="A")
    product_2 = Product.objects.create(name="B",
                                       price="2",
                                       discount_price="1",
                                       discount_number="2",
                                       discount_product="B")
    product_3 = Product.objects.create(name="C",
                                       price="3")
    product_4 = Product.objects.create(name="D",
                                       price="4",
                                       discount_price="2",
                                       discount_number="2",
                                       discount_product="E")
    product_5 = Product.objects.create(name="E",
                                       price="5")


class PriceTests(TestCase):
    """
    Test for price
    """
    def setUp(self):
        """
        Setup params
        """
        self.client = Client()
        insert_price()

    def test_price(self):
        response = self.client.get('/price/', {'a': '2', 'b': '0', 'c': '0', 'd': '0', 'e': '0'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '0.5')


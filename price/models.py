# -*- coding: utf-8 -*-
"""
Price models module
"""
from django.db import models


class Product(models.Model):
    """
    Product model
    """
    name = models.CharField('Product Name', max_length=15)
    price = models.FloatField('Price')
    discount_price = models.FloatField('Discount price', null=True,
                                         blank=True)
    discount_number = models.FloatField('Quantity of product', null=True,
                                          blank=True)
    discount_product = models.CharField('Product at a discount', max_length=5,
                                        null=True, blank=True)

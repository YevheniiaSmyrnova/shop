# -*- coding: utf-8 -*-
"""
Price admin module
"""
from django.contrib import admin

from price.models import Product


class ProductAdmin(admin.ModelAdmin):
    """
    Product admin
    """
    fieldsets = [
        ('Basic information', {'fields': ['name', 'price']}),
        ('Information about discounts', {'fields': ['discount_price',
                                                    'discount_number',
                                                    'discount_product']}),
    ]
    list_display = ('name', 'price')


admin.site.register(Product, ProductAdmin)

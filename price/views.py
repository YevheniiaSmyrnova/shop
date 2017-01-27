# -*- coding: utf-8 -*-
"""
Price views module
"""
from django.shortcuts import render

from price.forms import PriceForm
from price.models import Product


def price(request):
    """
    Calculate the price
    :param request: regular http(s) request
    :return: price
    """
    result = {}
    if request.GET:
        form = PriceForm(request.GET)
        if form.is_valid():
            products = {}
            products['A'] = form.cleaned_data['a']
            products['B'] = form.cleaned_data['b']
            products['C'] = form.cleaned_data['c']
            products['D'] = form.cleaned_data['d']
            products['E'] = form.cleaned_data['e']
            pr = 0

            for i in products.keys():
                if products[i] > 0:
                    product = Product.objects.get(name=i)
                    if product.name == product.discount_product:
                        if products[i] >= product.discount_number:
                            pr += product.discount_price * \
                                  (products[i] // product.discount_number) + \
                                  product.price * (products[i] % product.discount_number)
                        else:
                            pr += product.price * products[i]
                    elif not product.discount_product:
                        pr += round(product.price * products[i], 2)
                    else:
                        pr += product.price * products[i]
                        if products[i] >= product.discount_number and products[product.discount_product]:
                            product_discount = Product.objects.get(name=product.discount_product)
                            pr -= product_discount.price * products[product.discount_product]
                            if products[product.discount_product] > (products[
                                           i] // product.discount_number):
                                pr += product.discount_price * \
                                      (products[
                                      i] // product.discount_number) + \
                                      product_discount.price * (products[product.discount_product] - products[
                                      i] // product.discount_number)
                            else:
                                pr += product.discount_price * \
                                      (products[
                                      i] // product.discount_number)
            result['pr'] = pr

    else:
        form = PriceForm()
    result['form'] = form
    return render(request, 'price/index.html', result)


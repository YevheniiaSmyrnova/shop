# -*- coding: utf-8 -*-
"""
Price forms module
"""
from django import forms


class PriceForm(forms.Form):
    """
    Form for price
    """
    a = forms.IntegerField(label='Product A', initial=0)
    b = forms.IntegerField(label='Product B', initial=0)
    c = forms.FloatField(label='Product C', initial=0)
    d = forms.IntegerField(label='Product D', initial=0)
    e = forms.IntegerField(label='Product E', initial=0)

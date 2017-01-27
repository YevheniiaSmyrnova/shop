# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount_number',
            field=models.IntegerField(null=True, verbose_name=b'Quantity of product', blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='discount_price',
            field=models.IntegerField(null=True, verbose_name=b'Discount price', blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(verbose_name=b'Price'),
        ),
    ]

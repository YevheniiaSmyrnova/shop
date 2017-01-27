# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=15, verbose_name=b'Product Name')),
                ('price', models.CharField(max_length=10, verbose_name=b'Price')),
                ('discount_price', models.CharField(max_length=10, null=True, verbose_name=b'Discount price', blank=True)),
                ('discount_number', models.CharField(max_length=5, null=True, verbose_name=b'Quantity of product', blank=True)),
                ('discount_product', models.CharField(max_length=5, null=True, verbose_name=b'Product at a discount', blank=True)),
            ],
        ),
    ]

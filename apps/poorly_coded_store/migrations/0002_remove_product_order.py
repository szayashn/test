# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-08-20 18:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poorly_coded_store', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='order',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-22 10:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog_management', '0004_auto_20160722_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-17 15:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ship', '0014_auto_20161214_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soldier',
            name='tag',
            field=models.CharField(default='0x00 0x00 0x00 0x00', max_length=250),
        ),
    ]

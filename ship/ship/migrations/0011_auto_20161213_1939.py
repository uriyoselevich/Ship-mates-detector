# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-13 17:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ship', '0010_auto_20161213_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='singlerecord',
            name='time_stamp',
            field=models.CharField(max_length=250),
        ),
    ]

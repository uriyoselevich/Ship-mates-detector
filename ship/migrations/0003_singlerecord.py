# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-09 15:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ship', '0002_auto_20161209_1611'),
    ]

    operations = [
        migrations.CreateModel(
            name='SingleRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compartment', models.IntegerField(default=0)),
                ('time_stamp', models.IntegerField(default=0)),
                ('soldier_id', models.IntegerField(default=0)),
            ],
        ),
    ]

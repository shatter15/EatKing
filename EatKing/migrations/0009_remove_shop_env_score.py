# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-01 14:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EatKing', '0008_auto_20170701_2234'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop',
            name='env_score',
        ),
    ]
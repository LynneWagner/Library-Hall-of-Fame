# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-23 14:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0023_item_topic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='topic',
        ),
    ]
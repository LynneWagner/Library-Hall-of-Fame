# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-13 01:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0005_book_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
    ]

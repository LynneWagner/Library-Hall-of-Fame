# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-14 00:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0007_mags'),
    ]

    operations = [
        migrations.AddField(
            model_name='dvd',
            name='dvd_cover',
            field=models.CharField(default=0, max_length=1000),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-23 18:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0025_auto_20170623_1425'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.CharField(default=0, max_length=1000),
            preserve_default=False,
        ),
    ]

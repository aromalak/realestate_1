# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2022-12-21 04:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SHCS_app', '0031_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='token',
            name='token',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]

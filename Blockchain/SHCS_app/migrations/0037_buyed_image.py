# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2022-12-22 07:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SHCS_app', '0036_buyed'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyed',
            name='image',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]

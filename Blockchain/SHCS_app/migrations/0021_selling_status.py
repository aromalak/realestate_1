# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2022-12-17 07:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('SHCS_app', '0020_auto_20221215_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='selling',
            name='status',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]
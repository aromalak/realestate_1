# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2023-02-16 09:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SHCS_app', '0038_selling_hash1'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Buyed',
        ),
        migrations.DeleteModel(
            name='Requesttk',
        ),
        migrations.DeleteModel(
            name='Token',
        ),
        migrations.DeleteModel(
            name='Transaction',
        ),
        migrations.RemoveField(
            model_name='selling',
            name='token',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2022-12-15 11:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SHCS_app', '0018_selling'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sellings',
            fields=[
                ('r_id', models.IntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=255)),
                ('Ptype', models.CharField(max_length=255)),
                ('Prop_id', models.CharField(max_length=255)),
                ('details', models.CharField(max_length=255)),
                ('token', models.CharField(max_length=255)),
                ('image', models.CharField(max_length=255)),
                ('mobile', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Selling',
        ),
    ]

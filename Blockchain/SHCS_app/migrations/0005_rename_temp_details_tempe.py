# Generated by Django 4.1.3 on 2022-11-23 04:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("SHCS_app", "0004_details_delete_table_d_bp_delete_table_oxy_s_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="details", old_name="temp", new_name="tempe",
        ),
    ]

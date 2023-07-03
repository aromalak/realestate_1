# Generated by Django 4.1.5 on 2023-02-24 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("SHCS_app", "0041_selling_status"),
    ]

    operations = [
        migrations.CreateModel(
            name="Buyed",
            fields=[
                ("r_id", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255)),
                ("p_id", models.CharField(max_length=255)),
                ("hash1", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Transaction",
            fields=[
                ("r_id1", models.IntegerField(primary_key=True, serialize=False)),
                ("SName", models.CharField(max_length=255)),
                ("Saddr", models.CharField(max_length=255)),
                ("RName", models.CharField(max_length=255)),
                ("Raddr", models.CharField(max_length=255)),
                ("P_id", models.CharField(max_length=255)),
                ("Amount", models.CharField(max_length=255)),
                ("T_hash", models.CharField(max_length=255)),
            ],
        ),
    ]

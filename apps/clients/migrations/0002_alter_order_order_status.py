# Generated by Django 5.1.1 on 2024-09-13 13:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("clients", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="order_status",
            field=models.CharField(
                choices=[
                    ("Pending Dispatch", "Pending Dispatch"),
                    ("Dispatched", "Dispatched"),
                    ("Delivered", "Delivered"),
                ],
                default="Pending Dispatch",
                max_length=255,
            ),
        ),
    ]

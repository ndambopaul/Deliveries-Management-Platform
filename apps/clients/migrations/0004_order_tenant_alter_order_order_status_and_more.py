# Generated by Django 5.1.1 on 2024-09-13 14:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("clients", "0003_alter_order_customer_location"),
        ("tenants", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="tenant",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="tenants.tenant",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="order_status",
            field=models.CharField(
                choices=[
                    ("Created", "Created"),
                    ("Pending Dispatch", "Pending Dispatch"),
                    ("Dispatched", "Dispatched"),
                    ("Delivered", "Delivered"),
                ],
                default="Pending Dispatch",
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="orderstatusupdate",
            name="next_status",
            field=models.CharField(
                choices=[
                    ("Created", "Created"),
                    ("Pending Dispatch", "Pending Dispatch"),
                    ("Dispatched", "Dispatched"),
                    ("Delivered", "Delivered"),
                ],
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="orderstatusupdate",
            name="previous_status",
            field=models.CharField(
                choices=[
                    ("Created", "Created"),
                    ("Pending Dispatch", "Pending Dispatch"),
                    ("Dispatched", "Dispatched"),
                    ("Delivered", "Delivered"),
                ],
                max_length=255,
            ),
        ),
    ]
